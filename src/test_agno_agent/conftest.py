import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def _genai_test_session_setup():
    """
    Runs once before any tests in genai/tests start.
    Put any global setup here (e.g., env loading, logging config, etc.).
    """
    load_dotenv()

    # Add any other initialization you need here.
    # e.g., configure logging, set default environment variables, seed RNG, etc.

    yield

    # Optional: add global teardown logic here.
