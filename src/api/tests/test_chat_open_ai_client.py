import pytest
from langchain_core.messages import HumanMessage, AIMessage
from src.api.chat_open_ai_client import LangChainClient, OpenAIClientError


class TestChatOpenAIClient:
    def test_it_remembers_previous_messages(self, gpt_chat_mock):
        message = "Hi! I'm Lance."
        conversation_id = "Lance"
        config = {"configurable": {"thread_id": conversation_id}}

        gpt_chat_mock.return_value = {
            "messages": [
                HumanMessage(content="Hi. I'm Lance"),
                AIMessage(content="Hi Lance! How can I assist you today?"),
            ]
        }

        ai_client = LangChainClient()
        chat_response = ai_client.invoke(conversation_id, message)

        assert chat_response == "Hi Lance! How can I assist you today?"
        gpt_chat_mock.assert_called_once_with(config, [HumanMessage(message)])

    def test_it_raise_an_exception_when_lang_chain_client_fails(self, gpt_chat_mock):
        message = "Hi! I'm Lance."
        conversation_id = "Lance"
        ai_client = LangChainClient()

        gpt_chat_mock.side_effect = Exception

        with pytest.raises(OpenAIClientError):
            ai_client.invoke(conversation_id, message)
