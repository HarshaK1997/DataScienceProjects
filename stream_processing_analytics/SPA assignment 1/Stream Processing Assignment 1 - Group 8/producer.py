from kafka import KafkaProducer
import json
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

users = ["user1", "user2", "user3"]
locations = ["US", "IN", "UK", "CN"]

for _ in range(100):
    transaction = {
        "user_id": random.choice(users),
        "amount": random.uniform(10, 5000),
        "location": random.choice(locations),
    }
    producer.send("transactions", transaction)
    print(f"Sent: {transaction}")

producer.close()

