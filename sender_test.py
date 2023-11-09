from unittest.mock import patch
from fastapi.testclient import TestClient
from sender.sender import app
import responses

client = TestClient(app)

@patch('sender.sender.requests.post')
def test_ping_endpoint(mock_post):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == f'"pong"'
    mock_post.assert_not_called()

@patch('sender.sender.requests.post')
def test_send_message_endpoint_success(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"status": "Message received successfully by receiver service"}

    message = "Hello, World!"
    response = client.get(f"/send?message={message}")

    assert response.status_code == 200
    assert response.json() == {
        "status": "Message sent successfully by sender service",
        "response from receiver service": {"status": "Message received successfully by receiver service"}
    }

    mock_post.assert_called_once_with("http://receiver:8000/receive", json={"message": message})

@responses.activate
def test_send_message_endpoint_failure():
    message = "Hello, World!"
    url = "http://receiver:8000/receive"

    responses.add(responses.POST, url, json={"error": "Internal Server Error"}, status=500)

    response = client.get(f"/send?message={message}")

    assert response.json() == {"status": "Failed to send message"}

    # Assert that requests.post was called with the correct URL and JSON data
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert responses.calls[0].request.method == 'POST'
    assert responses.calls[0].response.status_code == 500
    assert responses.calls[0].response.text == '{"error": "Internal Server Error"}'
