# Overview
license-to-play is a repository to experiment with agentic AI

# Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
# sync dependencies
uv sync --all-groups

# add dependency
uv add langgraph
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
ruff check
ruff format
```

# LangGraph agents

```bash
# Run local LangGraph server
langgraph dev
```

This would make it available as:
* REST API: http://127.0.0.1:2024/docs
* Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
* Agent Chat UI: https://agentchat.vercel.app/
