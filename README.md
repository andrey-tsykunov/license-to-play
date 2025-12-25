# Overview
license-to-play is a repository to experiment with agentic AI

# Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
# sync dependencies
uv sync --all-groups

# add dependency
uv add langgraph
# add specific dependency version to dev group
uv add --dev "pytest==8.4.2"

# upgrade dependency
uv lock --upgrade-package langgraph

# show all dependencies
uv tree
# check dependencies
uv pip show PyYAML

# activate venv (windows)
.venv\Scripts\activate.bat
# activate venv (linux / macOS)
source .venv/bin/activate
# to run using venv
uv run python --version
```

Configure .env file based on .env.example

## Git Hooks

```bash
# Install pre-commit hooks
pre-commit install
# Run all hooks
pre-commit run --all-files
```

## Linters & Formatters

```bash
# To run linting manually
ruff check
ruff format
```

# LangGraph agents

[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) is a standalone library for building agents that can tackle complex, multi-step tasks. Built on LangGraph and inspired by applications like Claude Code, Deep Research, and Manus, deep agents come with planning capabilities, file systems for context management, and the ability to spawn subagents.

```bash
# Run local LangGraph server
langgraph dev
```

This would make it accessible via:
* REST API: http://127.0.0.1:2024/docs
* [LangSmith Studio](https://docs.langchain.com/langsmith/studio): https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
* [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui): https://agentchat.vercel.app/
* [Deep Agent UI](https://github.com/langchain-ai/deep-agents-ui): http://localhost:3000/

# Agno agents

[Agno](https://docs.agno.com/introduction) is an incredibly fast multi-agent framework, runtime and control plane.

```bash
fastapi dev src/agno_agent/agents.py
```

This would make it accessible via:
* REST API: http://127.0.0.1:8000/docs
* Agent OS Config: http://127.0.0.1:8000/config
* [Agno OS UI](https://docs.agno.com/agent-os/introduction): https://os.agno.com/
* [Agent UI](https://docs.agno.com/basics/agent-ui/overview): http://localhost:3000/

Alternatively, run directly with python:
```bash
PYTHONPATH=src python src/agno_agent/agents.py
````

This would make it accessible via:
* REST API: http://127.0.0.1:7777/docs
* etc


# MCP servers

## How to test / inspect MCP endpoints

Using [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
```bash
DANGEROUSLY_OMIT_AUTH=true npx @modelcontextprotocol/inspector

# Open http://localhost:6274/

# Set url (e.g. https://docs.agno.com/mcp) and click connect
```