import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# read in the data
df = pd.read_csv("C:\\Users\\Spyro\\Desktop\\FinTech -Analyst\\Python\\vgsales.csv")
df.dropna(inplace=True)
# group data by game name and sum global sales
game_sales = df.groupby('Name')['Global_Sales'].sum()
# sort by global sales
game_sales = game_sales.sort_values(ascending=False)
# display top 10 games
print(game_sales.head(10))
# group data by platform and sum global sales
platform_sales = df.groupby('Platform')['Global_Sales'].sum()
# sort by global sales
platform_sales = platform_sales.sort_values(ascending=False)
# display platform sales
print(platform_sales)
# group data by genre and sum global sales
genre_sales = df.groupby('Genre')['Global_Sales'].sum()
# sort by global sales
genre_sales = genre_sales.sort_values(ascending=False)
# display genre sales
print(genre_sales)
# create a bar chart showing sales by region
region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
region_sales.plot(kind='bar')
plt.title('Video Game Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales (millions)')
plt.show()
# create a scatter plot showing the relationship between year of release and global sales
plt.scatter(df['Year'], df['Global_Sales'])
plt.title('Year of Release vs Global Sales')
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.show()
# group data by publisher and sum global sales
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()
# sort by global sales
publisher_sales = publisher_sales.sort_values(ascending=False)
# create a bar chart showing top publishers by global sales
publisher_sales.head(10).plot(kind='bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()
# calculate mean and variance of global sales data
mean_sales = df['Global_Sales'].mean()
var_Sales = df['Global_Sales'].var()
# calculate expected mean and variance of Poisson distribution
exp_mean = var_Sales
exp_var = var_Sales
# compare mean and variance to expected values for Poisson distribution
print('Mean of global sales data:', mean_sales)
print('Variance of global sales data:', var_Sales)
print('Expected mean of Poisson distribution:', exp_mean)
print('Expected variance of Poisson distribution:', exp_var)
