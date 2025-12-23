import anthropic


def test_anthropic():
    # https://platform.claude.com/docs/en/about-claude/pricing
    # https://platform.claude.com/docs/en/about-claude/model-deprecations#model-status

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-haiku-4-5-20251001", max_tokens=1024, messages=[{"role": "user", "content": "Hello, Claude!"}]
    )

    print(message.content[0].text)
