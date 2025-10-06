'''
🧠 1. Sales Data Analysis Dashboard

Goal: Analyze a company’s monthly or yearly sales data.
What to do:

Load CSV with columns like Date, Product, Category, Quantity, Unit Price, Revenue.

Clean missing or incorrect data.

Group by month or category using groupby().

Create summary reports (total sales per product, most sold items, etc.).

Optional: visualize using Matplotlib/Seaborn.
Skills shown: data cleaning, aggregation, visualization.
Dataset idea: Kaggle - Superstore Sales Dataset
'''
import pandas as pd
import datetime 
import matplotlib.pyplot as plt
df = pd.read_csv("Superstore.csv", encoding="latin1")
df["Unit Price"] = df["Sales"] / df["Quantity"]
cloum = df[["Order Date", "Product Name", "Category", "Quantity", "Unit Price", "Sales"]]
# print(cloum.head(10)) 
#Cleaning data 
# print(df.duplicated().sum()) no duplicate
# print(cloum.info()) no missing data
# print("Checking zeror or negative values in Quantity")
# print(df[df["Quantity"] <= 0]) # Check zero or negative quantities
# print("Checking zeror or negative values in Sales")
# print(df[df["Sales"] <= 0])
# print(df.head())
print("Converting Order Date into date time and passing errors to check invalid dates Example:- NaT (Not a Time)")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Month"] = df["Order Date"].dt.to_period("M")
# print(df["Order Date"].head())
# print("check if any rows failed conversion")
#print(df[df["Order Date"].isna()]) checking missing or null values
total_sales_per_product = df.groupby(["Product Name"])["Sales"].sum().reset_index()
total_sales_per_product = total_sales_per_product.sort_values(by="Sales", ascending=False)
most_sold_items = df.groupby(["Product Name"])["Quantity"].sum().reset_index()
most_sold_items = most_sold_items.sort_values(by="Quantity", ascending=False)
# print(most_sold_items)
plt.figure(figsize=(12,6))
plt.barh(
    most_sold_items["Product Name"].head(10)[::-1],
    most_sold_items["Quantity"].head(10)[::-1],
    color='blue'
)
plt.xlabel("Units Sold")
plt.title("Top 10 Most Sold Products")
plt.show()





