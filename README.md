# Overview
license-to-play is a repository to experiment with agentic AI

**Project website:** https://andrey-tsykunov.github.io/license-to-play/

## Table of Contents

- [Setup](#setup)
  - [Git Hooks](#git-hooks)
  - [Linters & Formatters](#linters--formatters)
- [Agents](#agents)
- [Observability](#observability)
  - [Arize Phoenix](#arize-phoenix)
- [Web Frontend](#web-frontend)
  - [Local development](#local-development)
  - [Deploy to GitHub Pages](#deploy-to-github-pages)
- [MCP Servers](#mcp-servers)

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
uv lock --upgrade-package agno

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

# Agents

- [LangGraph agents](src/langgraph_agent/README.md)
- [Google ADK agents](src/google_adk_agent/README.md)
- [Agno agents](src/agno_agent/README.md)


# Observability

## Arize Phoenix
This project uses [Arize Phoenix](https://phoenix.arize.com/) for local observability and tracing.

To start the Phoenix server:

```bash
uv run python -m phoenix.server.main serve
```

This will make the UI available at: http://localhost:6006

# Web Frontend

The project has a React frontend in the `web/` directory, deployed to GitHub Pages.

## Local development

Requires [Node.js](https://nodejs.org/) 18+.

```bash
cd web
npm install
npm run dev
# Open http://localhost:5173/license-to-play/
```

## Deploy to GitHub Pages

```bash
cd web
npm run deploy
```

This builds the app and pushes to the `gh-pages` branch. Deployment also runs automatically via GitHub Actions on every push to `main` that touches `web/`.

# MCP servers

## How to test / inspect MCP endpoints

Using [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
```bash
DANGEROUSLY_OMIT_AUTH=true npx @modelcontextprotocol/inspector

# Open http://localhost:6274/

# Set url (e.g. https://docs.agno.com/mcp) and click connect
```