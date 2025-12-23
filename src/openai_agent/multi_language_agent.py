import asyncio

from agents import Agent, Runner, SQLiteSession
from dotenv import load_dotenv

from openai_agent.config import DEFAULT_AGENT_MODEL


def create_agent() -> Agent:
    spanish_agent = Agent(
        name="Spanish agent",
        model=DEFAULT_AGENT_MODEL,
        instructions="You only speak Spanish.",
    )

    english_agent = Agent(
        name="English agent",
        model=DEFAULT_AGENT_MODEL,
        instructions="You only speak English",
    )

    triage_agent = Agent(
        name="Triage agent",
        model=DEFAULT_AGENT_MODEL,
        instructions="Handoff to the appropriate agent based on the language of the request.",
        handoffs=[spanish_agent, english_agent],
    )

    return triage_agent


async def run():
    agent = create_agent()
    session = SQLiteSession("conversation_1")

    result = await Runner.run(agent, input="Hola, ¿cómo estás?", session=session)
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(run())
