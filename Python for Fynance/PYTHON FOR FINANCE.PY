import numpy as np
import pandas as pd
data = pd.read_csv('https://storage.googleapis.com/courses_data/Python%20for%20Finance/CAPM_Exercise_Data.csv', index_col = 'Date')
print(data.head())
print(data.tail())
returns = data.pct_change()
print(returns[:5])

alternative_returns = np.log(data/data.shift(1))
print(alternative_returns[:5])
cov = returns.cov() * 250
print(f'Covariance Matrix:\n\n{cov}\n')

covariance_with_market = cov.iloc[0,1]
print(f'Covariance of the stock with the market: {round(covariance_with_market, 6)}')

market_variance = returns['^GSPC'].var() * 250
print(f'Market Variance: {round(market_variance, 6)}')
MSFT_beta = covariance_with_market / market_variance
print(f'Microsoft beta factor: {round(MSFT_beta, 6)}')