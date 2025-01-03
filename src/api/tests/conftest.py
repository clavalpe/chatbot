from unittest.mock import patch
import pytest

from src.api.chat_open_ai_client import ChatOpenAIClient


@pytest.fixture(autouse=True)
def gpt_chat_mock():
    with patch.object(ChatOpenAIClient, "_invoke_chat") as mock:
        yield mock
