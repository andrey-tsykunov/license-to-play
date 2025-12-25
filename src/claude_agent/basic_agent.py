import asyncio

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from dotenv import load_dotenv

from claude_agent.config import DEFAULT_AGENT_MODEL


async def main():
    options = ClaudeAgentOptions(allowed_tools=["Bash", "Glob"], model=DEFAULT_AGENT_MODEL, cwd=".")

    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            prompt="What files are in this directory?",
        )

        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
