#%%
# import modules
import pandas as pd
import matplotlib.pyplot as plt


#%%
price_and_demand = pd.read_csv('PRICE_AND_DEMAND_202606_QLD1.csv', index_col= 'SETTLEMENTDATE', parse_dates=True)
print(price_and_demand)
#%%
# print plot the dataframe
# select action option
# 1 estimate the lowest price hours
price_and_demand['HOUR'] = price_and_demand.index.hour
negative_price = price_and_demand[price_and_demand['RRP'] < 0]
negative_price = negative_price.groupby('HOUR')['RRP'].mean().sort_values(ascending=True)
print(f"the lowest-price hours is: {negative_price.head(1).index[0]}")
negative_price.plot(kind='bar', color='red', title='Average Hour of Negative Price')
price_and_demand.groupby('HOUR')['RRP'].mean().plot(kind='bar', color='blue', title='Average Hour of Price')
# 2 plot the price in hour

# %%
