from agno.os import AgentOS
from agno.os.config import AgentOSConfig, ChatConfig
from agno.os.interfaces.a2a import A2A
from dotenv import load_dotenv
from loguru import logger

from agno_agent import agno_docs_agent, research_agent
from agno_agent.config import create_db, create_model
from agno_agent.math_agent import create_math_agent

load_dotenv()

model = create_model(max_tokens=16384)
db = create_db()

config = AgentOSConfig(
    chat=ChatConfig(
        quick_prompts={
            "math-agent": ["Add 3 and 4, then multiply by 2 and divide by 5"],
            "research-agent": ["What's the latest about OpenAIs GPT-5?"],
        }
    )
)

math_agent = create_math_agent(model, db)

agent_os = AgentOS(
    name="MyAgentOS 2",
    config=config,
    agents=[
        math_agent,
        agno_docs_agent.create_agent(model, db),
        research_agent.create_agent(model, db),
    ],
    interfaces=[A2A(agents=[math_agent])],
)

logger.info("Created Agent OS")

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agno_agent.server2:app", reload=True)
