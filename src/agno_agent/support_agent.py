from agno.agent import Agent
from agno.db import BaseDb
from agno.models.base import Model
from agno.team import Team


def create_support_agent(model: Model, agents: list[Agent], db: BaseDb):
    return Team(
        name="Support Agent",
        members=agents,
        model=model,
        db=db,
        # reasoning=True,
        instructions="""You are a support assistant used by bank advisor to help clients to resolve their problems.
    Clients may have various issues and inquiries related to their bank accounts, transactions, fees, and general banking services.
    In order to answer client questions, you have access to multiple agents which are specialized in different areas.

    Please use the following guideline when answering questions:
    - plan your steps before running the tools. Helping with user inquiry may require to chain multiple tool calls
    - format results returned from tools as the table if possible
    - if question is ambiguous ask for more information
    - be concise, don't repeat the same information multiple times (ie no need to summarize information if it's already provided earlier)
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
