import pytest
import yaml
from agno.client import AgentOSClient
from agno.db import SessionType
from agno.run.agent import RunCompletedEvent, RunContentEvent


@pytest.fixture(scope="module")
def client():
    return AgentOSClient(base_url="http://localhost:8000")


@pytest.fixture(scope="module")
def agent_id():
    return "agno-agent"


@pytest.fixture(scope="module")
def user_id():
    return "test-user"


@pytest.mark.asyncio
async def test_basic_interaction(client: AgentOSClient, agent_id: str, user_id: str):
    # Get configuration
    config = await client.aget_config()
    print("AgentOS Config\n", yaml.dump(config.model_dump()))

    session = await client.create_session(session_type=SessionType.AGENT, agent_id=agent_id, user_id=user_id)
    print(f"Created session: {session.session_id}")

    # # Send a message
    output = await client.run_agent(
        agent_id=agent_id, session_id=session.session_id, message="What is your special skill?"
    )
    print(f"Agent response: {output.content}\n")

    # Get session history
    history = await client.get_session_runs(session.session_id)
    print(f"Session has {len(history)} runs")


@pytest.mark.asyncio
async def test_streaming_response(client: AgentOSClient, agent_id: str, user_id: str):
    session = await client.create_session(session_type=SessionType.AGENT, agent_id=agent_id, user_id=user_id)
    print(f"Created session: {session.session_id}")

    async for event in client.run_agent_stream(
        agent_id=agent_id,
        session_id=session.session_id,
        message="What is your special skill?",
    ):
        if isinstance(event, RunContentEvent):
            print(event.content, end="", flush=True)
        elif isinstance(event, RunCompletedEvent):
            print(f"\nRun ID: {event.run_id}")


@pytest.mark.asyncio
async def test_list_agents(client: AgentOSClient):
    # List all agents
    agents = await client.list_agents()
    print(f"Available agents ({len(agents)}):")
    for agent in agents:
        print(f"  - {agent.id}: {agent.name}")

    if agents:
        agent_info = await client.aget_agent(agents[0].id)
        print(f"\nDetailed info for {agent_info.name}:")
        print(f"  Model: {agent_info.model.name}")
        print(f"  Description: {agent_info.description}")
        print(f"  Description: {agent_info.role}")
