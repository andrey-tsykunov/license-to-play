from agno.agent import Agent
from agno.db import BaseDb
from agno.models.base import Model
from agno.team import Team

from agno_agent.instructions import GENERAL_INSTRUCTIONS


def create_support_agent(model: Model, agents: list[Agent], db: BaseDb):
    return Team(
        name="Support Agent",
        members=agents,
        model=model,
        db=db,
        # reasoning=True,
        instructions=f"""You are a support assistant used by bank advisor to help clients to resolve their problems.
    Clients may have various issues and inquiries related to their bank accounts, transactions, fees, complains and general banking services.
    In order to answer client questions, you have access to multiple agents which are specialized in different areas.

{GENERAL_INSTRUCTIONS}
- use sub-agent definitions to decide which sub-agent to use to answer the question
- delegate the question to the most appropriate sub-agent as soon is theme is identified
    """,
        add_history_to_context=True,
        add_datetime_to_context=True,
        num_history_runs=5,
        respond_directly=True,
        determine_input_for_members=True,
        show_members_responses=True,
        stream_events=True,
        markdown=True,
    )
