import pytest
from agno.client.a2a import A2AClient


@pytest.mark.asyncio
async def test_a2a_client():
    # Connect to an Agno AgentOS A2A endpoint
    client = A2AClient("http://localhost:7777/a2a/agents/math-agent")

    # Send a message
    result1 = await client.send_message(message="add 10 and 1")
    print(f"{result1.context_id}: {result1.content}")

    result2 = await client.send_message(message="now add 2", context_id=result1.context_id)
    print(f"{result2.context_id}: {result2.content}")
    print(f"{result2.context_id}: {result1.content}")
