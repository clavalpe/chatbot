from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestIntegrationChatRoute:
    def test_chat_route_check(self):
        response = client.get("/chat")
        assert response.status_code == 200
        assert response.json() == {"assistant": "Hello! of course, let me know how I can help you!."}
