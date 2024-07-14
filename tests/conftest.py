from dotenv import load_dotenv
import pytest

from unittest.mock import AsyncMock
from os import environ

from pystepikconnect.client.synchronous import SyncStepik
from pystepikconnect.client.asynchronous import AsyncStepik


load_dotenv()


@pytest.fixture
def mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def client_id() -> str:
    return environ["TEST_ID"]


@pytest.fixture
def client_secret() -> str:
    return environ["TEST_SECRET"]


@pytest.fixture
def stepik(client_id: str, client_secret: str) -> SyncStepik:
    return SyncStepik(client_id=client_id, client_secret=client_secret)


@pytest.fixture
def async_stepik(client_id: str, client_secret: str) -> AsyncStepik:
    return AsyncStepik(client_id=client_id, client_secret=client_secret)
