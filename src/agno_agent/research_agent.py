from agno.agent import Agent
from agno.db import BaseDb
from agno.models.base import Model
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

from agno_agent.config import create_model


def create_agent(model: Model, db: BaseDb) -> Agent:
    return Agent(
        name="Research Agent",
        db=db,
        model=model,
        instructions="Conduct research and write very short report (no more than 5 sentences).",
        tools=[DuckDuckGoTools()],
        markdown=True,
    )


if __name__ == "__main__":
    load_dotenv()

    agent = create_agent(create_model())

    agent.print_response("What's the latest about OpenAIs GPT-5?", stream=True)
