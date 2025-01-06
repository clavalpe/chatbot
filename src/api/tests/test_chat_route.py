from fastapi.testclient import TestClient
from src.main import app
from langchain_core.messages import AIMessage, HumanMessage

client = TestClient(app)


class TestIntegrationChatRoute:
    def test_chat_route_check(self, gpt_chat_mock):
        gpt_chat_mock.return_value = {
            "messages": [
                HumanMessage(content="Hi, can you help me?"),
                AIMessage(content="Of course"),
            ]
        }

        input_data = {"user": "Hi, can you help me?"}

        expected_output = {"assistant": "Of course"}

        response = client.post("/chat", json=input_data)

        assert response.status_code == 200
        assert response.json() == expected_output

    def test_empty_message(self):
        input_data = {"user": ""}
        response = client.post("/chat", json=input_data)
        assert response.status_code == 500
