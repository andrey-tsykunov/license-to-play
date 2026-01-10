from agno.os import AgentOS
from agno.os.config import AgentOSConfig, ChatConfig
from agno.os.interfaces.agui import AGUI
from dotenv import load_dotenv

from agno_agent import agno_docs_agent, research_agent
from agno_agent.complain_agent import create_complain_agent, get_sample_complain_questions
from agno_agent.config import create_db, create_model
from agno_agent.fee_agent import create_fee_inquiry_agent, get_sample_fee_questions
from agno_agent.math_agent import create_math_agent
from agno_agent.support_agent import create_support_agent

load_dotenv()

model = create_model(max_tokens=16384)
db = create_db()

fee_agent = create_fee_inquiry_agent(model, db)
complain_agent = create_complain_agent(model, db)
support_team = create_support_agent(model, [fee_agent, complain_agent], db)
math_agent = create_math_agent(model)
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
    name="MyAgentOS",
    config=config,
    agents=[
        agno_docs_agent.create_agent(model),
        math_agent,
        research_agent.create_agent(model),
        fee_agent,
        complain_agent,
    ],
    teams=[support_team],
    interfaces=[AGUI(agent=math_agent)],  # optional for testing with AG-UI
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agno_agent.agents:app", reload=True)
