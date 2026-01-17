from agno.agent import RemoteAgent
from agno.os import AgentOS
from agno.os.config import AgentOSConfig, ChatConfig
from agno.os.interfaces.agui import AGUI
from dotenv import load_dotenv
from loguru import logger

from agno_agent.complain_agent import create_complain_agent, get_sample_complain_questions
from agno_agent.config import create_db, create_model
from agno_agent.fee_agent import create_fee_inquiry_agent, get_sample_fee_questions
from agno_agent.support_agent import create_support_agent

load_dotenv()

model = create_model(max_tokens=16384)
db = create_db()

fee_agent = create_fee_inquiry_agent(model, db)
complain_agent = create_complain_agent(model, db)
math_agent = RemoteAgent(
    base_url="http://localhost:7777",
    agent_id="math-agent",
)
support_team = create_support_agent(model, [fee_agent, complain_agent, math_agent], db)
config = AgentOSConfig(
    chat=ChatConfig(
        quick_prompts={
            "support-agent": [
                "Have client complained about NSF fees before?",
                "Have client reversed any fees in last 12 months?",
            ],
            "fee-inquiry-agent": get_sample_fee_questions(),
            "complain-agent": get_sample_complain_questions(),
        }
    )
)

agent_os = AgentOS(
    name="MyAgentOS 1",
    config=config,
    agents=[
        math_agent,
        RemoteAgent(
            base_url="http://localhost:7777",
            agent_id="agno-agent",
        ),
        fee_agent,
        complain_agent,
    ],
    teams=[support_team],
    interfaces=[AGUI(agent=fee_agent)],  # optional for testing with AG-UI
)

logger.info("Created Agent OS")

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agno_agent.agents:app", reload=True)
