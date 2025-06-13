# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 00:42:17 2025

@author: varra
"""

# Project Title: Sales Data Analysis for a Retail Company

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load Dataset
df = pd.read_csv(r"C:\Users\varra\OneDrive\Desktop\project\Sample - Superstore.csv", encoding='latin1')

# Preview Data
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())

# Check for nulls
print(df.isnull().sum())

# Drop columns not needed (optional)
df.drop(['Country', 'Postal Code'], axis=1, inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)


print(df.describe())

# Check unique values
print("Unique Categories:", df['Category'].unique())
print("Unique Segments:", df['Segment'].unique())


plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Category', y='Sales', estimator=sum)
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.show()

#top products by sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

top_products.plot(kind='bar', figsize=(10,6), title='Top 10 Products by Sales')
plt.ylabel("Sales")
plt.show()


plt.figure(figsize=(8,5))
sns.heatmap(df[['Sales', 'Quantity', 'Discount', 'Profit']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation between Sales Variables")
plt.show()


#pip install pandasql
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

# Total Sales by Region
query1 = "SELECT Region, SUM(Sales) as Total_Sales FROM df GROUP BY Region"
print(pysqldf(query1))

# Top 5 Customers by Profit
query2 = "SELECT [Customer Name], SUM(Profit) as Total_Profit FROM df GROUP BY [Customer Name] ORDER BY Total_Profit DESC LIMIT 5"
print(pysqldf(query2))


df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot(kind='line', figsize=(10,6), marker='o', title='Monthly Sales Trend')
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.show()




