from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "fraudalerts",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",  # Read from the beginning
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Listening for fraud alerts...")

for message in consumer:
    print(f"🚨 Fraud Alert: {message.value}")
