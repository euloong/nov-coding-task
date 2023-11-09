from fastapi import FastAPI

app = FastAPI()

# http://localhost:8002/ping
@app.get("/ping")
async def ping():
    print("Receiver service got pinged!")
    return "pong"

# http://receiver:8000/receive"
@app.post("/receive")
def receive_message(message: dict):
    received_message = message.get("message")
    if received_message:
        # Print the received message to stdout
        print("Received message from sender service:", received_message)
        return {"status": "Message received successfully by receiver service"}
    else:
        return {"status": "Invalid message format"}
