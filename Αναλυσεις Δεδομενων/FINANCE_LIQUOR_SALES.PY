import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import seaborn as sns
df = pd.read_csv("C:\\Users\\Spyro\\Desktop\\FinTech -Analyst\\Python\\finance_liquor_sales.csv")
#FILTER AND CLEANING

#DATE -> DATETIME
df["date"] = pd.to_datetime(df["date"])
# Remove the extra outer brackets and use () for each condition
filtered_df = df[(df["date"].dt.year >= 2016) & (df["date"].dt.year <= 2019)].reset_index(drop=True)
bottles_sold = filtered_df.groupby(["zip_code", "item_number"])["bottles_sold"].sum().reset_index()
filtered_df.info()
#ERGASIA A 
bottles_sold["zip_code"] = bottles_sold["zip_code"].astype(int)
idx = bottles_sold.groupby("zip_code")["bottles_sold"].idxmax()
max_bottles = bottles_sold.loc[idx].reset_index()
sorted_values = max_bottles.sort_values(by="bottles_sold", ascending=False).head(20)
plt.figure(figsize=(12, 7))
plt.bar(sorted_values["zip_code"].astype(str), sorted_values["bottles_sold"], color="skyblue")
plt.xlabel("Ταχυδρομικός Κώδικας")
plt.ylabel("Πωληθείσες Φιάλες")
plt.title("Μέγιστες Πωλήσεις Φιαλών ανά Ταχυδρομικό Κώδικα")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
#ERGASIA B
# Συνολικές πωλήσεις
total_sales = filtered_df["sale_dollars"].sum()
# Ομαδοποίηση ανά κατάστημα
sales_by_store = filtered_df.groupby("store_name")["sale_dollars"].sum()
#Ποσοστό
percentage_sales = (sales_by_store * 100 / total_sales).round(2)
top_15_stores = percentage_sales.sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 8))
p = plt.barh(top_15_stores.index, top_15_stores.values, color='lightcoral')
plt.xlabel("Ποσοστό Πωλήσεων (%)")
plt.title("Ποσοστό πωλήσεων ανά κατάστημα (Top 15)")
plt.gca().invert_yaxis()
plt.bar_label(p, fmt="%.2f%%")
plt.tight_layout()
plt.show()