import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
def poisson_probability(k, lam):
    return (lam ** k) * math.exp(-lam) / math.gamma(k + 1)
# read in the data
df = pd.read_csv("C:\\Users\\Spyro\\Desktop\\FinTech -Analyst\\Python\\vgsales.csv")
# compute the mean of the global sales data
mean_sales = np.mean(df['Global_Sales'])
# generate a histogram of the global sales data
n, bins, patches = plt.hist(df['Global_Sales'], bins=50, density=True, alpha=0.5)
# calculate the Poisson distribution for the mean
poisson_dist = [poisson_probability(b, mean_sales) for b in bins]
# plot the Poisson distribution over the histogram
plt.plot(bins, poisson_dist, 'r-', linewidth=2)
# label the plot
plt.title('Global Sales Data and Poisson Distribution')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Probability')
plt.show()