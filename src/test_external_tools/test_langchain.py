from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# MODEL_NAME = "gpt-5-nano"
MODEL_NAME = "gemma3:1b"
# MODEL_NAME = "llama3:8b"


def test_langchain_openai():
    chat = ChatOpenAI(model=MODEL_NAME, temperature=0)

    sys = SystemMessage(content="Summarize conversation between two individuals")
    msg1 = HumanMessage(content="Hi Mary, how are you?", name="Bob")
    msg2 = HumanMessage(content="Hey Bob, I am fine, how are you?", name="Mary")
    r = chat.invoke([sys, msg1, msg2])

    print(r.content)

    # Summary:
    # - Bob greets Mary and asks how she is.
    # - Mary replies that she is fine and asks Bob how he is.
