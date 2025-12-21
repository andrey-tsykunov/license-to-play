from langchain_openai import ChatOpenAI

from lg_deep_agent import math_agent
from lg_deep_agent.config import DEFAULT_AGENT_MODEL

llm = ChatOpenAI(model=DEFAULT_AGENT_MODEL)

math_agent_graph = math_agent.create_agent(llm)
