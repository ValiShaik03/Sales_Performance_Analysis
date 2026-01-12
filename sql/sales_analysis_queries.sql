-- Total sales and profit
SELECT SUM(sales), SUM(profit) FROM sales;

-- Sales by region
SELECT region, SUM(sales)
FROM sales
GROUP BY region
ORDER BY SUM(sales) DESC;

-- Loss making products
SELECT sub_category, SUM(profit)
FROM sales
GROUP BY sub_category
HAVING SUM(profit) < 0;
