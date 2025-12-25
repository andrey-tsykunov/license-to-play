import asyncio
from random import randint
from typing import Annotated

from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv
from pydantic import Field


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."


async def main() -> None:
    agent = OpenAIChatClient(model_id="gpt-5-nano").create_agent(
        instructions="You are a helpful weather agent.", tools=get_weather
    )

    async for chunk in agent.run_stream("What's the weather like in Portland?"):
        if chunk.text:
            print(chunk.text, end="", flush=True)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
