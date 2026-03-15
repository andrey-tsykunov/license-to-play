from crewai import Agent

from crewai_agent.config import create_llm


def create_researcher() -> Agent:
    return Agent(
        role="Technology Researcher",
        goal="Gather comprehensive factual information about a technology or framework",
        backstory=(
            "You are a senior technology researcher with 15 years of experience evaluating "
            "software frameworks and tools. You are known for thorough, unbiased research "
            "and always backing claims with concrete examples and real-world usage data."
        ),
        llm=create_llm(),
        verbose=True,
    )


def create_analyst() -> Agent:
    return Agent(
        role="Technical Analyst",
        goal="Critically evaluate technology trade-offs and identify ideal use cases",
        backstory=(
            "You are a principal engineer who has led architecture decisions at multiple "
            "companies. You excel at cutting through hype to identify where a technology "
            "genuinely shines and where it falls short, with concrete reasoning grounded "
            "in engineering principles."
        ),
        llm=create_llm(),
        verbose=True,
    )


def create_writer() -> Agent:
    return Agent(
        role="Technical Writer",
        goal="Produce a clear, well-structured evaluation report that engineers can act on",
        backstory=(
            "You are a technical writer who has produced documentation and evaluation reports "
            "for major open-source projects and engineering blogs. You transform raw research "
            "and analysis into concise, actionable reports that busy engineers actually read."
        ),
        llm=create_llm(),
        verbose=True,
    )
