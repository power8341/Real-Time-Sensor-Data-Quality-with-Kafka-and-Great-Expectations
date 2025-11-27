import pandas as pd
from great_expectations.dataset import PandasDataset

# Load sample CSV file
csv_path = "/Users/saiteja/Documents/Project_thesis/sample_sensor_data.csv"
df = pd.read_csv(csv_path)

# Wrap DataFrame with Great Expectations
ge_df = PandasDataset(df)

# Show first rows
print(ge_df.head())

# Optionally: run basic validation (if suite available)
# validation_results = ge_df.validate(expectation_suite_name="sensor_data_validation")
# print(validation_results)
