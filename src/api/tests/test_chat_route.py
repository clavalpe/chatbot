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
        assert response.status_code == 400

    def test_wrong_message_format(self):
        input_data = {"users ": "Hi, can you help me?"}
        response = client.post("/chat", json=input_data)
        assert response.status_code == 422

    def test_long_message(self):
        long_message = "a" * 10000
        response = client.post("/chat", json={"user": long_message})
        assert response.status_code == 400

    def test_returns_error_message_when_chabot_service_is_not_available(self, gpt_chat_mock):
        gpt_chat_mock.side_effect = Exception

        input_data = {"user": "Hi, can you help me?"}

        expected_output = {"detail": "The chatbot service is currently unavailable. Please try again later."}

        response = client.post("/chat", json=input_data)

        assert response.status_code == 500
        assert response.json() == expected_output
