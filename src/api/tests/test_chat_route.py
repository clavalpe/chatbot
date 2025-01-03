from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestIntegrationChatRoute:
    def test_chat_route_check(self):
        input_data = {"user": "Hi, can you help me with something?"}

        expected_output = {
            "assistant": "Hello! of course, let me know how I can help you!."
        }

        response = client.post("/chat", json=input_data)

        assert response.status_code == 200
        assert response.json() == expected_output
