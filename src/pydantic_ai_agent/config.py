import os


def get_default_model() -> str:
    """Return the default model name from env, defaulting to Claude Haiku."""
    return os.environ.get("DEFAULT_AGENT_MODEL", "claude-haiku-4-5-20251001")


def get_pydantic_ai_model() -> str:
    """Return a pydantic-ai model string for the configured provider."""
    name = get_default_model()
    if name.startswith("claude"):
        return f"anthropic:{name}"
    elif name.startswith("gpt") or name.startswith("o1") or name.startswith("o3"):
        return f"openai:{name}"
    elif name.startswith("gemini"):
        return f"google-gla:{name}"
    else:
        return f"ollama:{name}"
