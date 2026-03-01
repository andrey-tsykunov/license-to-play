import asyncio

from dotenv import load_dotenv
from google.adk import Runner
from google.adk.agents.llm_agent import Agent
from google.adk.sessions import InMemorySessionService
from google.genai import types


# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


def create_agent() -> Agent:
    return Agent(
        model="gemini-3-flash-preview",
        name="root_agent",
        description="Tells the current time in a specified city.",
        instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
        tools=[get_current_time],
    )


async def run():
    session_service = InMemorySessionService()
    session = await session_service.create_session(state={}, app_name="my_app", user_id="user_1")
    runner = Runner(app_name="my_app", agent=create_agent(), session_service=session_service)

    query = "What time is it in New York?"
    content = types.Content(role="user", parts=[types.Part.from_text(text=query)])

    print(f"User: {query}")
    async for event in runner.run_async(session_id=session.id, user_id="user_1", new_message=content):
        # Extract and print text from the final response event
        if event.is_final_response():
            for part in event.content.parts:
                if part.text:
                    print(f"Agent: {part.text}")


if __name__ == "__main__":
    load_dotenv()

    asyncio.run(run())
