from fastapi import FastAPI
import redis


app = FastAPI()
r = redis.Redis(host="redis", port=6379)


@app.post("/publish")
def publish(messageText: str):
    r.publish(channel="main", message=messageText)
