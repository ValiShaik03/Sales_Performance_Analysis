import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned data
df = pd.read_csv("data/processed/superstore_cleaned.csv")

# Ensure output directory exists
os.makedirs("outputs/charts", exist_ok=True)

# ===============================
# 1️⃣ Sales by Region
# ===============================
plt.figure(figsize=(8, 5))
df.groupby('Region')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/charts/sales_by_region.png")
plt.close()   # 🔥 VERY IMPORTANT

# ===============================
# 2️⃣ Monthly Sales Trend
# ===============================
plt.figure(figsize=(8, 5))
monthly_sales = df.groupby('Month')['Sales'].sum().sort_index()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("outputs/charts/monthly_sales_trend.png")
plt.close()   # 🔥 VERY IMPORTANT

print("✅ All charts generated successfully")