from unittest.mock import patch
import pytest

from src.api.chat_open_ai_client import LangChainClient


@pytest.fixture(autouse=True)
def gpt_chat_mock():
    with patch.object(LangChainClient, "_invoke_chat") as mock:
        yield mock
