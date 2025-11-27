from kafka import KafkaConsumer
import json
import pandas as pd
import great_expectations as ge
import uuid

# Initialize Great Expectations context
context = ge.get_context()
suite_name = "source_data_validation"
suite = context.get_expectation_suite(suite_name)

consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='sensor_data_validation_group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Starting Kafka consumer with GE validation and automated Data Docs updates...")

validation_count = 0

for message in consumer:
    data = message.value
    df = pd.DataFrame([data])
    ge_df = ge.dataset.PandasDataset(df)

    validation_result = ge_df.validate(expectation_suite=suite)

    # You can add saving validation results via checkpoint or other approach here if desired

    validation_count += 1

    # Build Data Docs every 10 validations
    if validation_count % 10 == 0:
        context.build_data_docs()
        print("Data Docs updated")

    if validation_result.success:
        print(f"Valid  {data}")
    else:
        print(f"Validation failed: {data}")
        print(validation_result)
