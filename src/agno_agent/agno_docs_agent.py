from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.base import Model
from agno.tools.mcp import MCPTools


def create_agent(model: Model) -> Agent:
    return Agent(
        name="Agno Agent",
        model=model,
        # Add a database to the Agent
        db=SqliteDb(db_file="./.agno/agno_docs.db"),
        # Add the Agno MCP server to the Agent
        tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
        # Add the previous session history to the context
        add_history_to_context=True,
        markdown=True,
    )
