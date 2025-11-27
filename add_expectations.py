import great_expectations as gx
from great_expectations.core import ExpectationConfiguration

# Initialize Great Expectations context
context = gx.get_context()

# Name of your expectation suite (use the exact name you created)
suite_name = "source_data_validation"
suite = context.get_expectation_suite(suite_name)

# Define expectations as ExpectationConfiguration objects
expectations = [
    ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "sensor_id"}
    ),
    ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_between",
        kwargs={"column": "temperature", "min_value": 15, "max_value": 50}
    ),
    ExpectationConfiguration(
        expectation_type="expect_column_values_to_be_between",
        kwargs={"column": "humidity", "min_value": 0, "max_value": 100}
    ),
    ExpectationConfiguration(
        expectation_type="expect_column_values_to_not_be_null",
        kwargs={"column": "timestamp"}
    )
]

# Add expectations to the suite
for expectation in expectations:
    suite.add_expectation(expectation)

# Save the updated expectation suite
context.save_expectation_suite(suite)

print(f"Expectation suite '{suite_name}' updated and saved successfully!")
