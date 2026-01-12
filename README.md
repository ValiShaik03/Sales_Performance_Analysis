# 📊 Sales Performance Analysis

## 📌 Project Overview
This project performs an end-to-end analysis of retail sales data to
understand revenue drivers, profitability issues, regional performance,
and seasonal trends.  
The analysis follows a real-world, production-style workflow similar to
what a Data Analyst would use in an organization.

---

## 🎯 Objective
To analyze sales data and answer key business questions such as:
- Which regions and products generate the most revenue?
- Which products are causing profit losses?
- Are there seasonal patterns in sales?
- How can the business improve profitability?

---

## 🗂 Project Structure
```
Sales-Performance-Analysis/
│
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned dataset
│
├── src/
│ ├── data_cleaning.py # Data cleaning & preprocessing
│ ├── analysis.py # Business analysis
│ └── visualization.py # Charts & visualizations
│
├── outputs/
│ ├── charts/ # Generated images
│ └── summary_report.txt # Final insights & recommendations
│
├── dashboard/
│ └── sales_dashboard.pbix
│
├── requirements.txt
└── README.md
```


---

## 🧾 Dataset Description
• Dataset Type: Retail / Superstore Sales  
• Size: ~50,000 records  
• Key Columns:
- Order_Date
- Region
- Category / Sub_Category
- Sales
- Profit
- Quantity
- Discount

---

## 🔧 Tools & Technologies
- **Python**: Pandas, Matplotlib
- **SQL**: Aggregation and business queries
- **Excel**: Initial inspection
- **Power BI**: Interactive dashboard

---

## 🧹 Data Cleaning Steps
- Handled non-UTF-8 file encoding
- Standardized column names
- Removed duplicate records
- Removed missing values
- Converted date columns to datetime format
- Created new features (Month, Year, Profit Margin)

---

## 📈 Analysis Performed
- Total sales and profit calculation
- Region-wise sales comparison
- Top 10 products by revenue
- Monthly sales trend analysis
- Identification of loss-making products

---

## 📊 Visualizations
- Sales by Region (Bar Chart)
- Monthly Sales Trend (Line Chart)
- KPI Metrics (via Power BI)

All charts are saved automatically in the `outputs/charts/` directory.

---

## 🔍 Key Insights
- A small percentage of products contribute to a majority of sales.
- Some categories show negative profitability despite high sales.
- Clear seasonal trends are visible across months.
- Regional performance varies significantly.

---

## 💡 Business Recommendations
- Focus on high-margin product categories.
- Optimize discount strategies to reduce losses.
- Plan inventory and promotions based on seasonal demand.
- Strengthen presence in high-performing regions.

---

## ▶️ How to Run the Project

# Step 1: Clean data
```
python src/data_cleaning.py
```
# Step 2: Run analysis
```
python src/analysis.py
```
# Step 3: Generate visualizations
```
python src/visualization.py
```

🧠 Key Learnings

- Handling real-world data issues like encoding and inconsistent columns

- Writing reusable and fault-tolerant data pipelines

- Translating raw data into actionable business insights

- Structuring projects in an industry-ready format


