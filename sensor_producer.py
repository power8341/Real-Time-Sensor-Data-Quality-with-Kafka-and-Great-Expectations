from kafka import KafkaProducer
import json
import time
import random

# Connect to Kafka broker running locally
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_sensor_data():
    # Simulate some sensor metrics with random values
    return {
        "sensor_id": f"sensor_{random.randint(1,10)}",
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
    }

if __name__ == "__main__":
    while True:
        data = generate_sensor_data()
        producer.send('sensor_data', value=data)
        print(f"Sent  {data}")
        time.sleep(2)  # Send data every 2 seconds
