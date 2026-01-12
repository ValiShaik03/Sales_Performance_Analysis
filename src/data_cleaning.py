import pandas as pd
import os

# 🔹 Get absolute project root (VERY IMPORTANT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
RAW_PATH = os.path.join(BASE_DIR, "data", "raw", "superstore_raw.csv")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "superstore_cleaned.csv")

# Read CSV
df = pd.read_csv(RAW_PATH, encoding="latin1")

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("Standardized Columns:")
print(df.columns)

# Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Feature engineering
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month
df['Year'] = df['Order_Date'].dt.year
df['Profit_Margin'] = df['Profit'] / df['Sales']

# 🔥 Ensure folder exists
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Save file (ABSOLUTE PATH)
df.to_csv(OUTPUT_FILE, index=False)

print("✅ Data cleaning completed successfully")
print("📁 File saved at:", OUTPUT_FILE)
