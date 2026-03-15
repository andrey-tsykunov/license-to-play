# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**license-to-play** is an agentic AI experimentation repository that implements the same core agents (math, research, support) across multiple frameworks for comparison: Agno, LangGraph, Google ADK, Claude SDK, and OpenAI/Microsoft Agents.

## Development Commands

### Dependencies
```bash
uv sync --all-groups          # Install all dependencies
uv add <package>              # Add dependency
uv add --dev <package>        # Add dev dependency
```

### Linting & Formatting
```bash
ruff check                    # Run linter
ruff format                   # Format code
```

### Testing
```bash
pytest -s src                 # Run all tests (no output capture)
pytest -s src/test_agno_agent # Run specific test directory
pytest -s src/test_agno_agent/test_rest.py  # Run single test file
```

### Running Agents

**Agno:**
```bash
fastapi dev src/agno_agent/server1.py               # Port 8000 (AgentOS UI)
fastapi dev --port 7777 src/agno_agent/server2.py   # Port 7777 (REST API)
PYTHONPATH=src python src/agno_agent/server2.py     # Direct execution
```

**LangGraph:**
```bash
langgraph dev   # Port 2024, uses langgraph.json config
```

**Google ADK:**
```bash
adk run src/google_adk_agent
adk web src
```

**Observability (Arize Phoenix):**
```bash
uv run python -m phoenix.server.main serve   # http://localhost:6006
```

## Architecture

### Multi-Framework Pattern
Each agent framework lives in its own `src/<framework>_agent/` directory. Most implement the same agents (math, research) to enable cross-framework comparison. The consistent internal pattern is:
- `config.py` — model factory + SQLite DB creation
- Agent files — agent creation functions
- `server.py` / entry points — FastAPI or framework-specific server

### Agent Frameworks

**Agno** (`src/agno_agent/`) — most fully-featured implementation
- Multi-agent team with AgentOS orchestration
- Agents: fee_agent, complain_agent, math_agent, support_agent, research_agent, agno_docs_agent
- REST API via FastAPI + A2A (Agent-to-Agent) interface
- Skills in `src/agno_agent/skills/` directory (complain, fee-inquiry)
- SQLite persistence via `.agno/agno.db`

**LangGraph** (`src/langgraph_agent/`)
- StateGraph-based orchestration, `graphs.py` defines `math_agent` and `agent` (research)
- Configured via `langgraph.json`

**Google ADK** (`src/google_adk_agent/`)
- root_agent + time_agent using google.adk framework and Gemini models

**Claude SDK** (`src/claude_agent/`)
- Async streaming agent using Anthropic's Claude Agent SDK

**OpenAI/Microsoft** (`src/openai_agent/`, `src/microsoft_agent/`)
- Multi-language agent with handoff capabilities, session-based

### Model Support
All agents support multiple providers via environment config:
- `DEFAULT_AGENT_MODEL` env var (default: `claude-haiku-4-5-20251001`)
- Claude (Anthropic), GPT (OpenAI), Ollama (local)

### Required Environment Variables
Copy `.env.example` to `.env` and populate:
- `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GOOGLE_API_KEY`
- `TAVILY_API_KEY` (web search), `FIRECRAWL_API_KEY` (scraping)
- `LANGSMITH_API_KEY`, `PERPLEXITY_API_KEY`
- `DEFAULT_AGENT_MODEL` (optional override)

### Observability
Arize Phoenix + OpenTelemetry tracing is instrumented across frameworks. Start Phoenix before running agents to capture traces.

### Pre-commit Hooks
```bash
pre-commit install            # One-time setup
pre-commit run --all-files    # Manual run
```
Hooks run ruff lint + format automatically on commit.
