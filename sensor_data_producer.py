from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    return {
        "sensor_id": f"sensor_{random.randint(1, 5)}",
        "temperature": round(random.uniform(15, 50), 1),
        "humidity": round(random.uniform(20, 80), 1),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    data = generate_sensor_data()
    producer.send('sensor_data', data)
    print(f"Sent: {data}")
    time.sleep(1)
