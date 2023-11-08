from fastapi import FastAPI
import requests

app = FastAPI()

RECEIVER_API_URL = "http://receiver:8000/receive"  # URL of the receiver endpoint inside the Docker network

# http://localhost:8001/ping
@app.get("/ping")
async def ping():
    print("Sender service got pinged!")
    return "pong"


# http://localhost:8001/send
@app.get("/send")
def send_message(message: str):
    # Post the message to the receiver service
    response = requests.post(RECEIVER_API_URL, json={"message": message})
    if response.status_code == 200:
        return {"status": "Message sent successfully by sender service", "response from receiver service": response.json()}
    else:
        return {"status": "Failed to send message"}, 500
