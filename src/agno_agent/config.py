import os
from typing import Optional

from agno.db import BaseDb
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.models.base import Model
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat

DEFAULT_AGENT_MODEL = os.environ.get("DEFAULT_AGENT_MODEL", "claude-sonnet-4-20250514")


def create_model(name: str = DEFAULT_AGENT_MODEL, max_tokens: Optional[int] = None) -> Model:
    if name.startswith("claude"):
        return Claude(id=name, max_tokens=max_tokens or 4096)
    elif name.startswith("gpt"):
        return OpenAIChat(id=name, max_tokens=max_tokens or 4096)
    else:
        if max_tokens is not None:
            raise ValueError("Ollama model does not support max_tokens parameter")
        return Ollama(id=name)


def create_db() -> BaseDb:
    return SqliteDb(db_file="./.agno/agno.db")
