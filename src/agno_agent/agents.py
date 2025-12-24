from agno.os import AgentOS
from agno.os.config import AgentOSConfig, ChatConfig
from dotenv import load_dotenv

from agno_agent import agno_docs_agent, math_agent, research_agent
from agno_agent.config import create_db, create_model
from agno_agent.support_agent import create_support_agent

load_dotenv()

model = create_model()
db = create_db()

support_team = create_support_agent(model, db)

config = AgentOSConfig(
    chat=ChatConfig(
        quick_prompts={
            "support-agent": [
                "Client wants to reverse a fee charged in august",
                "What are recent credit card Walmart transactions",
                "Did client reversed any fees in the past?",
            ]
        }
    )
)

agent_os = AgentOS(
    name="MyAgentOS",
    config=config,
    agents=[
        agno_docs_agent.create_agent(model),
        math_agent.create_agent(model),
        research_agent.create_agent(model),
    ],
    teams=[support_team],
)
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()
