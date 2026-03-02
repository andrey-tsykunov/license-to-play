import httpx
import pytest
from a2a.client import (
    Client,
    ClientConfig,
    ClientFactory,
    create_text_message_object,
)
from a2a.types import Artifact, Message, Task
from a2a.utils.message import get_message_text
from agno.client.a2a import A2AClient


@pytest.mark.asyncio
async def test_a2a_using_agno_client():
    # Connect to an Agno AgentOS A2A endpoint
    client = A2AClient("http://localhost:7777/a2a/agents/math-agent")
    print(client.get_agent_card())

    # Send a message
    result1 = await client.send_message(message="add 10 and 1")
    print(f"{result1.context_id}: {result1.content}")

    result2 = await client.send_message(message="now add 2", context_id=result1.context_id)
    print(f"{result2.context_id}: {result2.content}")


@pytest.mark.asyncio
async def test_a2a_using_native_a2a_client():
    async with httpx.AsyncClient(timeout=100.0) as httpx_client:
        client: Client = await ClientFactory.connect(
            "http://localhost:7777/a2a/agents/math-agent",
            client_config=ClientConfig(
                httpx_client=httpx_client,
            ),
        )

        agent_card = await client.get_card()
        print(agent_card)

        message = create_text_message_object(content="add 10 and 1")

        async for response in client.send_message(message):
            if isinstance(response, Message):
                # The agent replied directly with a final message
                print(f"Message ID: {response.message_id}")
                text_content = get_message_text(response)
            # response is a ClientEvent
            elif isinstance(response, tuple):
                task: Task = response[0]
                print(f"Task ID: {task.id}, status: {task.status}")
                if task.artifacts:
                    artifact: Artifact = task.artifacts[0]
                    print(f"Artifact ID: {artifact.artifact_id}")
                    text_content = get_message_text(artifact)

        print(text_content)

        # a2a.client.errors.A2AClientInvalidStateError: Invalid state error: received a streamed Message from server after first response; this is not supported
