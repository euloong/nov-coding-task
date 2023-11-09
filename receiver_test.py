from fastapi.testclient import TestClient
from receiver.receiver import app

client = TestClient(app)

def test_ping_endpoint():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == f'"pong"'

def test_receive_message_endpoint_success():
    message = {"message": "Hello, World!"}
    response = client.post("/receive", json=message)
    assert response.status_code == 200
    assert response.json() == {"status": "Message received successfully by receiver service"}

def test_receive_message_endpoint_invalid_format():
    invalid_message = {"invalid_key": "Hello, World!"}
    response = client.post("/receive", json=invalid_message)
    assert response.json() == {"status": "Invalid message format"}

def test_receive_message_endpoint_missing_message():
    missing_message = {}
    response = client.post("/receive", json=missing_message)
    assert response.json() == {"status": "Invalid message format"}
