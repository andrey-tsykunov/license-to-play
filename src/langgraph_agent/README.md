# LangGraph agents

[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents.

[Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) is a standalone library for building agents that can tackle complex, multi-step tasks. Built on LangGraph and inspired by applications like Claude Code, Deep Research, and Manus, deep agents come with planning capabilities, file systems for context management, and the ability to spawn subagents.

```bash
# Run local LangGraph server
langgraph dev
```

This would make it accessible via:
* REST API: http://127.0.0.1:2024/docs
* [LangSmith Studio](https://docs.langchain.com/langsmith/studio): https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
* [Agent Chat UI](https://github.com/langchain-ai/agent-chat-ui): https://agentchat.vercel.app/
* [Deep Agent UI](https://github.com/langchain-ai/deep-agents-ui): http://localhost:3000/
