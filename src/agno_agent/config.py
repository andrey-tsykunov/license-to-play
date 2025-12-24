import os
from typing import Optional

from agno.db import BaseDb
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.models.base import Model
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat


def get_default_model() -> str:
    return os.environ.get("DEFAULT_AGENT_MODEL", "claude-haiku-4-5-20251001")


def create_model(name: Optional[str] = None, max_tokens: Optional[int] = None) -> Model:
    if name is None:
        name = get_default_model()

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
