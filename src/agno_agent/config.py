from agno.models.anthropic import Claude
from agno.models.base import Model
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat

# DEFAULT_AGENT_MODEL = "llama3.1:8b"
DEFAULT_AGENT_MODEL = "claude-haiku-4-5-20251001"
# DEFAULT_AGENT_MODEL = "claude-sonnet-4-20250514"


def create_model(name: str = DEFAULT_AGENT_MODEL) -> Model:
    if name.startswith("claude"):
        return Claude(id=name)
    elif name.startswith("gpt"):
        return OpenAIChat(id=name)
    else:
        return Ollama(id=name)
