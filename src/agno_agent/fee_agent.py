from dataclasses import dataclass
from datetime import datetime

from agno.agent import Agent
from agno.db import BaseDb
from agno.models.base import Model
from agno.tools import tool
from dotenv import load_dotenv

from agno_agent.config import create_db, create_model


@tool(requires_confirmation=True)
def reverse_transaction(id: str) -> bool:
    """Reverse fee by transaction id. Only transactions with type "fee" can be reversed. User need to confirm the action

    Args:
        id: id of the transaction to reverse

    Returns:
        bool: True if the transaction was reversed, False otherwise
    """

    # comment_from_advisor: Comment from advisor why the transaction is being reversed (to be reported to compliance)
    if id == "CT0008":
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
    return [ReversalInfo("CT0004", datetime(2025, 6, 3, 9, 0), datetime(2025, 7, 2, 11, 0), -10.0)]


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


def fetch_transactions(account_id: str, type: str | None) -> list[TransactionInfo]:
    """Fetch recent transactions for a given account.

    Args:
        account_id: The ID of the account to fetch transactions for.
        type: Transaction type filter (e.g. "fee", "e-transfer", "purchase", "withdrawal", "payment"). If None, fetch all types.

    Returns:
        list[TransactionInfo]: list of transactions (id, type, name, timestamp, balance)
    """
    data = {
        "C00001": [
            TransactionInfo("CT0001", "purchase", "Amazon", datetime(2025, 6, 1, 10, 0), -50.0),
            TransactionInfo("ST0002", "withdrawal", "ATM Withdrawal", datetime(2025, 6, 2, 11, 0), -100.0),
            TransactionInfo("CT0003", "e-transfer", "John Doe", datetime(2025, 6, 2, 12, 30), -200.0),
            TransactionInfo("CT0004", "fee", "Monthly Maintenance", datetime(2025, 6, 3, 9, 0), -10.0),
            TransactionInfo("CT0005", "deposit", "Paycheck", datetime(2025, 7, 1, 15, 0), 1500.0),
            TransactionInfo("CT0006", "fee", "Monthly Maintenance", datetime(2025, 7, 3, 9, 0), -10.0),
            TransactionInfo("CT0007", "deposit", "Paycheck", datetime(2025, 8, 1, 15, 0), 1500.0),
            TransactionInfo("CT0008", "fee", "Monthly Maintenance", datetime(2025, 8, 3, 9, 0), -10.0),
        ],
        "S00001": [
            TransactionInfo("ST0001", "deposit", "Transfer", datetime(2025, 3, 1, 15, 0), 1500.0),
        ],
        "CR00001": [
            TransactionInfo("CRT0003", "purchase", "TTC", datetime(2025, 5, 1, 14, 0), -50.0),
            TransactionInfo("CRT0004", "purchase", "AirCanada", datetime(2025, 5, 1, 14, 0), -800.0),
            TransactionInfo("CRT0005", "purchase", "Amazon", datetime(2025, 5, 1, 14, 0), -35.0),
            TransactionInfo("CRT0006", "purchase", "Walmart", datetime(2025, 6, 1, 14, 0), -75.0),
            TransactionInfo("CRT0007", "purchase", "Walmart", datetime(2025, 6, 1, 14, 1), -10.0),
            TransactionInfo("CRT0008", "payment", "Credit Card Payment", datetime(2025, 6, 3, 16, 0), 900.0),
            TransactionInfo("CRT0009", "fee", "Credit Card Fee", datetime(2025, 7, 3, 16, 0), 100.0),
        ],
    }

    transactions = data.get(account_id)

    if transactions is None:
        raise Exception(f"Account {account_id} not found")

    transactions = [t for t in transactions if type is None or t.type == type]

    return transactions


def create_fee_inquiry_agent(model: Model, db: BaseDb) -> Agent:
    return Agent(
        name="Fee Inquiry and Reversal Agent",
        model=model,
        db=db,
        instructions="""You are a support assistant *specialized* in transaction fee inquiries, explanation and reversal process.
Please use the following guideline when serving the client:
- plan your steps before running the tools. Helping with user inquiry may require to chain multiple tool calls
- format results returned from tools as a table
- client inquiry could be ambiguous. think if it could be disambiguated by checking some data using tools. If it is not possible, ask for more information
- if client is asking for reversal of a transaction, make sure to check if the transaction is of type "fee", other type of transactions cannot be reversed
- before proceeding with reversal provide a warning if the client already reversed fees in the past
- be concise, don't repeat the same information multiple times (ie no need to summarize information if it's already provided earlier)
""",
        #  UserControlFlowTools()
        tools=[reverse_transaction, accounts_list, fetch_transactions, previous_reversals],
        add_history_to_context=True,
        num_history_runs=5,
        # reasoning=True,
        markdown=True,
    )


def get_sample_fee_questions() -> list[str]:
    return [
        "Client wants to reverse a fee charged in august",
        "What are recent credit card transactions for Walmart",
        "Did client reverse any fees in the past?",
    ]


if __name__ == "__main__":
    load_dotenv()

    agent = create_fee_inquiry_agent(create_model(), create_db())

    agent.print_response("Reverse transaction 123", stream=True)
