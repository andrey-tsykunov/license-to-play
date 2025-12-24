import pytest
from ollama import Client
from openai import OpenAI


@pytest.fixture(scope="module")
def client() -> OpenAI:
    return OpenAI(
        base_url="http://localhost:11434/v1",  # Local Ollama API endpoint
    )


def test_ollama_via_openai_chat_api(client: OpenAI):
    response = client.chat.completions.create(
        model="gemma3:1b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The LA Dodgers won in 2020."},
            {"role": "user", "content": "Where was it played?"},
        ],
    )

    # E               openai.NotFoundError: 404 page not found
    #
    # .venv/lib/python3.13/site-packages/openai/_base_client.py:1047: NotFoundError

    print(response.choices[0].message.content)


def test_ollama_response_api(client: OpenAI):
    response = client.responses.create(
        model="gemma3:1b",
        input="write a haiku about ai",
        store=True,
    )
    # https://www.perplexity.ai/search/is-ollama-rest-api-compatible-xkKEB_z7TVucQIq5k7bJ_g
    # Ollama is OpenAI API compatible for the traditional chat completions endpoints but does not yet support
    # the newer OpenAI Responses API used for agent features and newer workflow interactions
    print(response.output_text)


def test_ollama_chat():
    client = Client()
    response = client.chat(
        model="llama3.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The LA Dodgers won in 2020."},
            {"role": "user", "content": "Where was it played?"},
        ],
    )

    print(response.message.content)


def test_ollama_web_search():
    client = Client()
    response = client.web_search("What is Ollama?")
    print(response)


def test_ollama_web_fetch():
    client = Client()
    response = client.web_fetch("https://ollama.com")
    print(response)
