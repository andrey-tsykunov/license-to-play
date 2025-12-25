import asyncio

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from dotenv import load_dotenv

from claude_agent.config import DEFAULT_AGENT_MODEL


async def message_stream():
    """Generate messages dynamically."""
    yield {"type": "text", "text": "Analyze the following data:"}
    await asyncio.sleep(0.5)
    yield {"type": "text", "text": "Temperature: 25°C"}
    await asyncio.sleep(0.5)
    yield {"type": "text", "text": "Humidity: 60%"}
    await asyncio.sleep(0.5)
    yield {"type": "text", "text": "What patterns do you see?"}


async def main():
    options = ClaudeAgentOptions(model=DEFAULT_AGENT_MODEL)

    async with ClaudeSDKClient(options=options) as client:
        # Stream input to Claude
        await client.query(message_stream())

        # Process response
        async for message in client.receive_response():
            print(message)

        # Follow-up in same session
        await client.query("Should we be concerned about these readings?")

        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())

    # claude_agent_sdk._errors.CLIConnectionError: Cannot write to terminated process (exit code: 1)
