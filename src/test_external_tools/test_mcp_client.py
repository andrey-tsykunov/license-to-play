import pytest
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


@pytest.mark.asyncio
async def test_agno_streamable_http_mcp():
    """Connect to Agno MCP or other Streamable HTTP server"""

    # https://modelcontextprotocol.io/docs/getting-started/intro
    # https://github.com/modelcontextprotocol/python-sdk

    url = "https://docs.agno.com/mcp"
    query = "What is Agno?"

    async with streamable_http_client(url) as (read, write, callbacks):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call a streaming tool
            print("\nCalling tool...")
            result = await session.call_tool(name="SearchAgno", arguments={"query": query, "max_results": 5})

            # Handle streaming content
            print("\nResults:")
            for item in result.content:
                if item.type == "text":
                    print(item.text)
                elif item.type == "resource":
                    print(f"Resource: {item.resource.uri}")
