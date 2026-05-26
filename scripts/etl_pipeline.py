import pandas as pd
import os

# -----------------------------
# 1. CREATE PATHS (VERY IMPORTANT)
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.abspath(
    os.path.join(base_dir, "..", "data", "raw", "sales.csv")
)
output_path = os.path.join(base_dir, "..", "data", "processed", "final_sales.csv")

# Ensure folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)


# 2. LOAD DATA

df = pd.read_csv(input_path)

print("✅ Data loaded:", df.shape)


# 3. CLEAN DATA

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df["order_date"] = pd.to_datetime(df["order_date"])

print("✅ Data cleaned")


# 4. FEATURE ENGINEERING

df["total_revenue"] = df["price"] * df["quantity"]
df["month"] = df["order_date"].dt.month
df["year"] = df["order_date"].dt.year

print("✅ Features created")


# 5. BUSINESS KPIs

print("\n📊 KPIs")
print("Total Revenue:", df["total_revenue"].sum())
print("Total Orders:", df["order_id"].nunique())
print("Total Customers:", df["customer_id"].nunique())


# 6. SAVE FILE (THIS WAS FAILING BEFORE)

df.to_csv(output_path, index=False)

print("\n✅ ETL completed successfully!")
print("📁 File saved at:")
print(os.path.abspath(output_path))