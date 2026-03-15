"""
Pydantic AI research agent — structured output showcase.

Unique capability: the agent returns a fully-validated, typed `ResearchReport`
Pydantic model instead of raw text, giving you IDE autocompletion, runtime
validation, and easy serialisation (e.g. to JSON/DB) for free.
"""

from __future__ import annotations

import asyncio
from datetime import date
from typing import Annotated

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from tavily import TavilyClient

from pydantic_ai_agent.config import get_pydantic_ai_model

# ── Structured output schema ──────────────────────────────────────────────────


class Source(BaseModel):
    title: str
    url: str
    relevance: Annotated[float, Field(ge=0.0, le=1.0, description="Relevance score 0-1")]


class ResearchReport(BaseModel):
    """Fully-typed research report returned by the agent."""

    topic: str = Field(description="The research topic")
    summary: str = Field(description="Concise executive summary (2-3 sentences)")
    key_findings: list[str] = Field(
        description="List of 3-5 most important findings",
        min_length=1,
        max_length=5,
    )
    sources: list[Source] = Field(
        description="Sources consulted, ordered by relevance",
        min_length=1,
    )
    confidence: Annotated[
        float,
        Field(ge=0.0, le=1.0, description="Agent's confidence in the report (0-1)"),
    ]
    generated_on: date = Field(
        default_factory=date.today,
        description="Date the report was generated",
    )


# ── Agent dependencies ─────────────────────────────────────────────────────────


class ResearchDeps(BaseModel):
    tavily_client: TavilyClient

    model_config = {"arbitrary_types_allowed": True}


# ── Agent definition ───────────────────────────────────────────────────────────


def create_research_agent(model: str | None = None) -> Agent[ResearchDeps, ResearchReport]:
    model_name: str = model or get_pydantic_ai_model()

    agent: Agent[ResearchDeps, ResearchReport] = Agent(
        model_name,  # type: ignore[arg-type]
        deps_type=ResearchDeps,
        output_type=ResearchReport,
        system_prompt=(
            "You are a precise research assistant. "
            "Use the web_search tool to gather current information, "
            "then synthesise your findings into a structured report. "
            "Always cite your sources and be honest about your confidence level."
        ),
    )

    @agent.tool
    async def web_search(
        ctx: RunContext[ResearchDeps],
        query: str,
        max_results: int = 5,
    ) -> str:
        """Search the web for up-to-date information on a topic.

        Args:
            query: The search query.
            max_results: Maximum number of results to return (1-10).
        """
        response = ctx.deps.tavily_client.search(
            query=query,
            max_results=max_results,
            include_answer=True,
        )
        lines: list[str] = []
        if response.get("answer"):
            lines.append(f"Summary: {response['answer']}\n")
        for r in response.get("results", []):
            lines.append(f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content'][:400]}\n")
        return "\n---\n".join(lines) or "No results found."

    return agent


# ── Run helpers ────────────────────────────────────────────────────────────────


async def run_research(topic: str, model: str | None = None) -> ResearchReport:
    """Run the research agent and return a typed ResearchReport."""
    import os

    deps = ResearchDeps(tavily_client=TavilyClient(api_key=os.environ["TAVILY_API_KEY"]))
    agent = create_research_agent(model)
    result = await agent.run(f"Research the following topic: {topic}", deps=deps)
    return result.output


# ── CLI entry point ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import json
    import sys

    load_dotenv()

    topic = " ".join(sys.argv[1:]) or "Pydantic AI framework features and use cases"
    print(f"Researching: {topic}\n")

    report = asyncio.run(run_research(topic))

    # The result is a fully-typed, validated Pydantic model
    print("=" * 60)
    print(f"TOPIC:      {report.topic}")
    print(f"CONFIDENCE: {report.confidence:.0%}")
    print(f"DATE:       {report.generated_on}")
    print()
    print("SUMMARY:")
    print(f"  {report.summary}")
    print()
    print("KEY FINDINGS:")
    for i, finding in enumerate(report.key_findings, 1):
        print(f"  {i}. {finding}")
    print()
    print("SOURCES:")
    for source in report.sources:
        print(f"  [{source.relevance:.0%}] {source.title}")
        print(f"         {source.url}")
    print()
    print("JSON (e.g. for API response / DB storage):")
    print(json.dumps(report.model_dump(mode="json"), indent=2))
