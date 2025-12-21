# license-to-play
Repository to experiment with agentic AI

# Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
# sync dependencies
uv sync --all-groups

# add dependency
uv add langgraph
uv add --dev "pytest==8.4.2"

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