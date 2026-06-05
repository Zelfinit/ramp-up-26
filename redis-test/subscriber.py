import redis

r = redis.Redis(host="localhost", port=6379)
pubsub = r.pubsub()
pubsub.subscribe("main")
for message in pubsub.listen():
    if message["type"] == "message":
        print(message["data"].decode())
