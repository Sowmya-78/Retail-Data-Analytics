import pandas as pd
import sqlite3
import os

# 1. LOAD CLEAN DATA

file_path = "../data/processed/final_sales.csv"
df = pd.read_csv(file_path)

print("✅ Data loaded:", df.shape)

# 2. CREATE SQLITE DATABASE

conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

# 3. LOAD DATA INTO SQL TABLE

df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Data loaded into SQL database")

# 4. RUN BUSINESS QUERIES

# Total revenue
query1 = "SELECT SUM(total_revenue) FROM sales;"
print("\n💰 Total Revenue:", pd.read_sql(query1, conn))

# Revenue by category
query2 = """
SELECT category, SUM(total_revenue) as revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;
"""
print("\n📦 Category Revenue:\n", pd.read_sql(query2, conn))

# Top regions
query3 = """
SELECT region, SUM(total_revenue) as revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;
"""
print("\n🌍 Region Revenue:\n", pd.read_sql(query3, conn))

# Monthly trend
query4 = """
SELECT month, SUM(total_revenue) as revenue
FROM sales
GROUP BY month
ORDER BY month;
"""
print("\n📅 Monthly Trend:\n", pd.read_sql(query4, conn))

# Top customers
query5 = """
SELECT customer_id, SUM(total_revenue) as revenue
FROM sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10;
"""
print("\n🏆 Top Customers:\n", pd.read_sql(query5, conn))

# 5. CLOSE CONNECTION

conn.close()

print("\n✅ SQL analysis completed successfully!")