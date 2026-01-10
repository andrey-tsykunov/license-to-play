from dataclasses import dataclass
from datetime import datetime

from agno.agent import Agent
from agno.db import BaseDb
from agno.models.base import Model
from agno.run import RunContext
from agno.tools import tool
from dotenv import load_dotenv

from agno_agent.config import create_db, create_model
from agno_agent.instructions import GENERAL_INSTRUCTIONS


@tool(requires_confirmation=True)
def submit_complain(run_context: RunContext, complain_summary: str) -> str:
    client_id = run_context.session_state.get("client_id")

    print(f"Submitted complain for {client_id} client")


@dataclass
class ComplainInfo:
    id: str
    timestamp: datetime
    summary: str


def infer_complain_summary_from_transcript(run_context: RunContext) -> str:
    client_id = run_context.session_state.get("client_id")

    print(f"Inferring complain summary from transcript for {client_id} client")

    return "Client complained about bad weather"


def fetch_complains(run_context: RunContext) -> list[ComplainInfo]:
    client_id = run_context.session_state.get("client_id")

    print(f"Fetching complains for {client_id} client")

    return [
        ComplainInfo(
            "CMP0001",
            datetime(2025, 4, 1, 14, 0),
            "Client complained about unexpected credit card fees on their account",
        ),
        ComplainInfo(
            "CMP0001", datetime(2025, 5, 1, 14, 0), "Client complained about unexpected NSF fees on their account"
        ),
        ComplainInfo(
            "CMP0001", datetime(2025, 6, 1, 14, 0), "Client complained about unexpected NSF fees on their account"
        ),
        ComplainInfo("CMP0002", datetime(2025, 12, 1, 14, 0), "Client reported issues with online banking access."),
    ]


def get_sample_complain_questions() -> list[str]:
    return [
        "What is a common reason for this client to submit complains?",
        "Did client submit any complains in last 3 months? Provide advice how to avoid these fees in the future",
        "Submit complain",
    ]


def create_complain_agent(model: Model, db: BaseDb) -> Agent:
    return Agent(
        name="Complain Agent",
        description="An agent specialized in handling customer complains.",
        model=model,
        db=db,
        instructions=f"""You are a support assistant *specialized* in dealing with customer complains.
{GENERAL_INSTRUCTIONS}
- you should try to infer complain summary from the transcript by default, but ask confirmation from the advisor before submitting the complain.
- advisor could always override complain summary and provide it directly
""",
        #  UserControlFlowTools()
        tools=[fetch_complains, submit_complain, infer_complain_summary_from_transcript],
        add_history_to_context=True,
        add_datetime_to_context=True,
        num_history_runs=5,
        # reasoning=True,
        markdown=True,
        session_state={"client_id": "client-000001"},
    )


if __name__ == "__main__":
    load_dotenv()

    agent = create_complain_agent(create_model(), create_db())

    agent.print_response("What is most recent complain from the client?", stream=True)
