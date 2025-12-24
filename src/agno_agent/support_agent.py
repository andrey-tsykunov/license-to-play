from dataclasses import dataclass
from datetime import datetime

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.base import Model
from agno.tools import tool
from agno.tools.user_control_flow import UserControlFlowTools
from dotenv import load_dotenv

from agno_agent.config import create_model


@tool(requires_confirmation=True)
def reverse_transaction(id: str, comment_from_advisor: str) -> bool:
    """Reverse fee by transaction id. Only transactions with type "fee" can be reversed. User need to confirm the action

    Args:
        id: id of the transaction to reverse
        comment_from_advisor: Comment from advisor why the transaction is being reversed (to be reported to compliance)

    Returns:
        bool: True if the transaction was reversed, False otherwise
    """
    if id == "CT0005":
        return True
    return False


@dataclass
class ReversalInfo:
    transaction_id: str
    transaction_timestamp: datetime
    reversal_timestamp: datetime
    amount: float


def previous_reversals() -> list[ReversalInfo]:
    """Returns previous reversals for the client

    Returns:
        list[ReversalInfo]: list of previous reversals (transaction_id, transaction_timestamp, reversal_timestamp and amount)
    """
    return [ReversalInfo("CT0003", datetime(2025, 6, 3, 9, 0), datetime(2025, 7, 2, 11, 0), 10.0)]


@dataclass
class AccountInfo:
    id: str
    name: str
    balance: float


def accounts_list() -> list[AccountInfo]:
    """Get information about client accounts (id, name and balance)

    Returns:
        list[AccountInfo]: list of accounts (id, name and balance)
    """
    return [
        AccountInfo("C00001", "Checking", 1000.0),
        AccountInfo("S00001", "Savings", 5000.0),
        AccountInfo("CR00001", "Platinum Visa Credit card", 1456.0),
    ]


@dataclass
class TransactionInfo:
    id: str
    type: str
    name: str
    timestamp: datetime
    amount: float


def fetch_transactions(account_id: str, type: str | None) -> list[dict]:
    """Fetch recent transactions for a given account.

    Args:
        account_id: The ID of the account to fetch transactions for.
        type: Transaction type filter (e.g. "fee", "e-transfer", "purchase", "withdrawal"). If None, fetch all types.

    Returns:
        list[TransactionInfo]: list of transactions (id, type, name, timestamp, balance)
    """
    data = {
        "C00001": [
            TransactionInfo("CT0001", "purchase", "Amazon", datetime(2025, 6, 1, 10, 0), -50.0),
            TransactionInfo("CT0002", "e-transfer", "John Doe", datetime(2025, 6, 2, 12, 30), -200.0),
            TransactionInfo("CT0003", "fee", "Monthly Maintenance", datetime(2025, 6, 3, 9, 0), -10.0),
            TransactionInfo("CT0004", "fee", "Monthly Maintenance", datetime(2025, 7, 3, 9, 0), -10.0),
            TransactionInfo("CT0005", "fee", "Monthly Maintenance", datetime(2025, 8, 3, 9, 0), -10.0),
        ],
        "S00001": [
            TransactionInfo("ST0004", "deposit", "Paycheck", datetime(2025, 6, 1, 15, 0), 1500.0),
            TransactionInfo("ST0005", "withdrawal", "ATM Withdrawal", datetime(2025, 6, 2, 11, 0), -100.0),
        ],
        "CR00001": [
            TransactionInfo("CRT0006", "purchase", "Walmart", datetime(2025, 6, 1, 14, 0), -75.0),
            TransactionInfo("CRT0007", "purchase", "Walmart", datetime(2025, 6, 1, 14, 1), -10.0),
            TransactionInfo("CRT0008", "payment", "Credit Card Payment", datetime(2025, 6, 3, 16, 0), 300.0),
        ],
    }

    transactions = data.get(account_id)

    if transactions is None:
        raise Exception(f"Account {account_id} not found")

    transactions = [t for t in transactions if type is None or t.type == type]

    return transactions


def create_agent(model: Model) -> Agent:
    return Agent(
        name="Support Agent",
        model=model,
        db=SqliteDb(db_file="./.agno/agno_support.db"),
        instructions="""You are a support assistant used by bank advisor to help clients to resolve their problems.
Please use the following guideline when answering questions:
- try to plan your steps before running the tool. Helping the user may require to chain multiple tool calls
- try to format results returned from tools as the table if possible
- if question is ambiguous ask for more information
- if client is asking for reversal of a transaction, make sure to check if the transaction is of type "fee" and provide a warning if the client already reversed fees in the past
- be concise, don't repeat the same information multiple times
        """,
        tools=[reverse_transaction, accounts_list, fetch_transactions, previous_reversals, UserControlFlowTools()],
        add_history_to_context=True,
        num_history_runs=5,
        markdown=True,
    )


if __name__ == "__main__":
    load_dotenv()

    agent = create_agent(create_model())

    agent.print_response("Reverse transaction 123", stream=True)
