from agno.agent import Agent
from agno.models.base import Model
from dotenv import load_dotenv

from agno_agent.config import create_model


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


def create_agent(model: Model) -> Agent:
    return Agent(
        name="Math Agent",
        model=model,
        instructions="You are a helpful assistant tasked with performing arithmetic on a set of inputs.",
        tools=[multiply, add, divide],
        markdown=True,
    )


if __name__ == "__main__":
    load_dotenv()

    agent = create_agent(create_model("llama3.1"))

    agent.print_response("Add 3 and 4, then multiply by 2 and divide by 5")
