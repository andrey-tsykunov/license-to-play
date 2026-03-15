import os

from crewai import LLM


def get_default_model() -> str:
    return os.environ.get("DEFAULT_AGENT_MODEL", "claude-haiku-4-5-20251001")


def create_llm() -> LLM:
    model = get_default_model()
    # CrewAI uses litellm; Anthropic models need the provider prefix
    if model.startswith("claude") and not model.startswith("anthropic/"):
        model = f"anthropic/{model}"
    return LLM(model=model)
