from agno.os import AgentOS
from dotenv import load_dotenv

from agno_agent import agno_docs_agent, math_agent, research_agent, support_agent
from agno_agent.config import create_model

load_dotenv()

model = create_model()

# Create the AgentOS
agent_os = AgentOS(
    agents=[
        agno_docs_agent.create_agent(model),
        math_agent.create_agent(model),
        research_agent.create_agent(model),
        support_agent.create_agent(model),
    ]
)
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()
