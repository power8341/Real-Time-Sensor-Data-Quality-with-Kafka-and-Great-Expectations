#!/usr/bin/env python3
import great_expectations as gx
import sys
import os
import pandas as pd
import numpy as np
import great_expectations.exceptions as gx_exceptions

context = gx.get_context()
print("🔍 Checking prerequisites...")

# 1. Create sample data if missing
if not os.path.exists('sample_sensor_data.csv'):
    print("📊 Creating sample_sensor_data.csv...")
    data = [{'sensor_id':f's{i}', 'temperature':np.random.uniform(20,50), 'humidity':np.random.uniform(40,100), 'timestamp':'2025-11-27T12:00:00'} for i in range(100)]
    pd.DataFrame(data).to_csv('sample_sensor_data.csv', index=False)
    print("✅ CSV created!")

# 2. Load data and create fresh validation EVERY TIME (bulletproof)
print("📊 Loading data for validation...")
df = pd.read_csv('sample_sensor_data.csv')

# 3. Create PandasDataset with expectations DIRECTLY (no suite loading needed)
ge_df = gx.from_pandas(df)

# 4. Add expectations and validate in ONE GO
ge_df.expect_column_values_to_not_be_null('sensor_id')
ge_df.expect_column_values_to_be_between('temperature', 15, 50)
ge_df.expect_column_values_to_be_between('humidity', 30, 100)

# 5. Validate (CORRECT parameter name)
result = ge_df.validate()  # No suite needed - uses built-in expectations

success = result.success
print(f"✅ RESULT: {'PASSED ✅' if success else 'FAILED ❌'}")
print(f"📈 Expectations passed: {sum(1 for e in result.results if e.success)}/{len(result.results)}")

sys.exit(0 if success else 1)
