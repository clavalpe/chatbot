from fastapi.testclient import TestClient
from chatbot_routes import app

client = TestClient(app)

class TestIntegrationChatBotRoutes:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}