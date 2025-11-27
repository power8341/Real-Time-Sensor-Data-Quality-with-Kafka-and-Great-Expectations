from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # start from the earliest message
    enable_auto_commit=True,
    group_id='sensor-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Starting consumer, listening to 'sensor_data' topic...")

for message in consumer:
    data = message.value
    print(f"Received sensor  {data}")
