from langchain_core.messages import HumanMessage, AIMessage

from src.api.chat_open_ai_client import LangChainClient


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
