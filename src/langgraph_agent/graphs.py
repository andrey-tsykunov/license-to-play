from langchain_openai import ChatOpenAI
from tavily import TavilyClient

from langgraph_agent import math_agent, research_agent
from langgraph_agent.config import DEFAULT_AGENT_MODEL

llm = ChatOpenAI(model=DEFAULT_AGENT_MODEL)
tavily_client = TavilyClient()

math_agent_graph = math_agent.create_agent(llm)
research_agent_graph = research_agent.create_agent(llm, tavily_client)
