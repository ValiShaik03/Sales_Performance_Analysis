import pandas as pd

df = pd.read_csv("data/processed/superstore_cleaned.csv")

# Total metrics
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())

# Region-wise analysis
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)

# Top products
top_products = df.groupby('Sub_Category')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)
