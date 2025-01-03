from langchain_core.messages import HumanMessage, AIMessage

from src.api.chat_open_ai_client import ChatOpenAIClient


class TestChatOpenAIClient:
    def test_it_replies_a_human_message(self, gpt_chat_mock):
        message = "Hi, can you help me?"
        gpt_chat_mock.return_value = AIMessage(content="Of course")

        chat_response = ChatOpenAIClient().invoke(message)

        assert chat_response == "Of course"
        gpt_chat_mock.assert_called_once_with(
            [HumanMessage(content=message, name="Lance")]
        )
