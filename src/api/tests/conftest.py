from unittest.mock import patch
import pytest

from src.api.chat_open_ai_client import LangChainClient
from langchain_core.messages import HumanMessage, AIMessage


@pytest.fixture(autouse=True)
def gpt_chat_mock():
    with patch.object(LangChainClient, "_invoke_chat") as mock:
        mock.return_value = {
            "messages": [
                HumanMessage(content="Hi. I'm Lance"),
                AIMessage(content="Hi Lance! How can I assist you today?"),
            ]
        }
        yield mock
