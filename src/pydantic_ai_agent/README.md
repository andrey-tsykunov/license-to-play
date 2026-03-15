# Pydantic AI Agent

A research agent built with [Pydantic AI](https://ai.pydantic.dev/) that showcases its most distinctive capability: **structured, type-safe outputs**.

## Unique capability — structured typed outputs

Unlike other frameworks that return raw text or untyped dicts, Pydantic AI lets you declare a Pydantic model as the `output_type`. The framework:

1. Generates a JSON schema from your model and sends it to the LLM
2. Validates the response at runtime — invalid responses are retried automatically
3. Returns a **fully typed Python object** with IDE autocompletion and static analysis support

```python
class ResearchReport(BaseModel):
    topic: str
    summary: str
    key_findings: list[str]
    sources: list[Source]
    confidence: float          # validated 0.0–1.0
    generated_on: date

agent = Agent("anthropic:claude-haiku-4-5-20251001", output_type=ResearchReport)
result = await agent.run("Research Pydantic AI")
report: ResearchReport = result.output   # ← fully typed, IDE-friendly
```

## Agents

| Agent | File | Description |
|-------|------|-------------|
| Research Agent | `research_agent.py` | Searches the web via Tavily and returns a typed `ResearchReport` |

## Running

```bash
# Install dependencies
uv sync --all-groups

# Configure .env (needs ANTHROPIC_API_KEY + TAVILY_API_KEY)
cp .env.example .env

# Run on a topic
PYTHONPATH=src python src/pydantic_ai_agent/research_agent.py "agentic AI frameworks 2025"
```

## Multi-provider support

Set `DEFAULT_AGENT_MODEL` in `.env` to switch providers:

```bash
DEFAULT_AGENT_MODEL=claude-haiku-4-5-20251001   # Anthropic (default)
DEFAULT_AGENT_MODEL=gpt-4o-mini                  # OpenAI
DEFAULT_AGENT_MODEL=gemini-2.0-flash             # Google
```
