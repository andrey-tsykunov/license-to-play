import pytest
from agno.agent import RemoteAgent
from agno.team import RemoteTeam


@pytest.mark.asyncio
async def test_remote_agent():
    # Create a remote agent pointing to a remote AgentOS instance
    agent = RemoteAgent(
        base_url="http://localhost:8000",
        agent_id="math-agent",
    )

    # Run the agent (async)
    response = await agent.arun("Add 20 and 30")
    print(response.content)


@pytest.mark.asyncio
async def test_remote_team():
    # Create a remote agent pointing to a remote AgentOS instance
    agent = RemoteTeam(
        base_url="http://localhost:8000",
        team_id="support-agent",
    )

    # Run the agent (async)
    response = await agent.arun("Add 2 and 3")
    print(response.content)

    # 'RemoteAgent' object has no attribute 'output_schema'
    # https://kyushu-edu-hinds.blogspot.com/?page=en-git-agno-agi-agno-1768030364573
