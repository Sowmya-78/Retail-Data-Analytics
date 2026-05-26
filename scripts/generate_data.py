import pandas as pd
import numpy as np
import os

# 1. CREATE FOLDERS AUTOMATICALLY

base_path = os.path.join("..", "data")
raw_path = os.path.join(base_path, "raw")
processed_path = os.path.join(base_path, "processed")

os.makedirs(raw_path, exist_ok=True)
os.makedirs(processed_path, exist_ok=True)

print("✅ Folders created successfully")

# 2. GENERATE SAMPLE DATA

np.random.seed(42)

n = 50000  # dataset size

df = pd.DataFrame({
    "order_id": np.arange(1, n + 1),
    "order_date": pd.date_range(start="2023-01-01", periods=n, freq="H"),
    "product_id": np.random.randint(1000, 1100, n),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], n),
    "price": np.round(np.random.uniform(10, 500), 2),
    "quantity": np.random.randint(1, 5, n),
    "customer_id": np.random.randint(10000, 20000, n),
    "region": np.random.choice(["North", "South", "East", "West"], n)
})


# 3. FEATURE ENGINEERING

df["revenue"] = df["price"] * df["quantity"]

# 4. SAVE FILES

raw_file = os.path.join(raw_path, "sales.csv")
processed_file = os.path.join(processed_path, "sales_cleaned.csv")

df.to_csv(raw_file, index=False)
df.to_csv(processed_file, index=False)

print("✅ Dataset created and saved successfully!")
print("📁 Raw file:", raw_file)
print("📁 Processed file:", processed_file)