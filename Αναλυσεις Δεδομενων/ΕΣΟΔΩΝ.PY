import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load the dataset
data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
        'Revenue': [100, 200, 150, 300, 120, 250, 170, 350, 110, 280]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
# Perform basic statistical analysis
total_revenue = np.sum(df['Revenue'])
average_daily_revenue = np.mean(df['Revenue'])
product_revenue = df.groupby('Product')['Revenue'].sum()
print("Total Revenue: ", total_revenue)
print("Average Daily Revenue: ", average_daily_revenue)
print("Total Revenue per Product:\n", product_revenue)
# Bar chart of total revenue per product
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
product_revenue.plot(kind='bar')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.title('Total Revenue per Product')
plt.xticks(rotation=0)
# Line chart of daily revenue
plt.subplot(1, 2, 2)
plt.plot(df['Date'], df['Revenue'])
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.title('Daily Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()