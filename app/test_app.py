from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_post_chat():
    response = client.post("/chat", json={"prompt": "Hello, what is AI?"})
    assert response.status_code == 200
    assert "response" in response.json()
