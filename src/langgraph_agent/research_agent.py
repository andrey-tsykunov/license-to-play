# https://github.com/langchain-ai/deepagents-quickstarts/tree/main/deep_research
from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.state import CompiledStateGraph
from tavily import TavilyClient

from langgraph_agent.config import DEFAULT_AGENT_MODEL


def create_agent(llm: ChatOpenAI, tavily_client: TavilyClient) -> CompiledStateGraph:
    def internet_search(query: str, max_results: int = 5):
        """Run a web search"""
        return tavily_client.search(query, max_results=max_results)

    agent = create_deep_agent(
        model=llm,
        tools=[internet_search],
        system_prompt="Conduct research and write very short report (no more than 5 sentences).",
    )

    return agent


def run() -> None:
    llm = ChatOpenAI(model=DEFAULT_AGENT_MODEL)
    tavily_client = TavilyClient()
    agent = create_agent(llm, tavily_client)

    messages = [HumanMessage(content="What is LangGraph?")]

    result = agent.invoke({"messages": messages})

    for m in result["messages"]:
        m.pretty_print()


if __name__ == "__main__":
    load_dotenv()
    run()
