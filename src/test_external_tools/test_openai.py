from openai import OpenAI


def test_openai_chat_api():
    # https://platform.openai.com/docs/models

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-5-nano",
        # model="gemma3:1b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "write a haiku about ai"},
        ],
    )

    print(response.choices[0].message.content)


def test_openai_response_api():
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5-nano",
        # model="gemma3:1b",
        input="write a haiku about ai",
        store=True,
    )

    print(response.output_text)
