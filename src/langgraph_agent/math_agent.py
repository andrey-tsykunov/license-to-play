# https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent-memory.ipynb

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.constants import START
from langgraph.graph import MessagesState
from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph_agent.config import DEFAULT_AGENT_MODEL


def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


# This will be a tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b


def create_agent(llm: ChatOpenAI) -> CompiledStateGraph:
    tools = [add, multiply, divide]
    llm_with_tools = llm.bind_tools(tools)

    # System message
    sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic on a set of inputs.")

    # Node
    def assistant(state: MessagesState):
        return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

    # Graph
    builder = StateGraph(MessagesState)

    # Define nodes: these do the work
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    # Define edges: these determine how the control flow moves
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant",
        # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
        # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
        tools_condition,
    )
    builder.add_edge("tools", "assistant")
    react_graph = builder.compile()

    return react_graph


def run() -> None:
    llm = ChatOpenAI(model=DEFAULT_AGENT_MODEL)
    graph = create_agent(llm)

    messages = [HumanMessage(content="Add 3 and 4, then multiply by 2 and divide by 5")]

    result = graph.invoke({"messages": messages})

    for m in result["messages"]:
        m.pretty_print()


if __name__ == "__main__":
    load_dotenv()
    run()
