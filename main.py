#%%
# import modules
import pandas as pd
import matplotlib.pyplot as plt


#%%
print("This program will help you to analyze the negative price in AEMO's NEM Price and demand data.")
print("Please make sure the csv file is available and has the following columns: SETTLEMENTDATE, RRP, DEMAND")
file = input("Please input a NEM's Price and demand csv file name: ")
price_and_demand = pd.read_csv(file, index_col= 'SETTLEMENTDATE', parse_dates=True)
if price_and_demand.empty:
    print("The csv file is empty. Please check the file and try again.")
    exit()
if not all(col in price_and_demand.columns for col in ['RRP', 'DEMAND']):
    print("The csv file does not have the required columns. Please check the file and try again.")
    exit()
print(price_and_demand)

#%%
# This part of the code is to confirm the period of the data
price_and_demand['MONTH'] = price_and_demand.index.month
if price_and_demand['MONTH'].sort_values(ascending = True).iloc[0] == price_and_demand['MONTH'].sort_values(ascending = False).iloc[0]:
    print(f"This data is observed in {price_and_demand['MONTH'].iloc[0]} ")
if price_and_demand['MONTH'].sort_values(ascending = True).iloc[0] != price_and_demand['MONTH'].sort_values(ascending = False).iloc[0]:
    print(f"This data is observed from {price_and_demand['MONTH'].sort_values(ascending = True).iloc[0]} to {price_and_demand['MONTH'].sort_values(ascending = False).iloc[0]} ")
#%%
# select action option
# 1 estimate the lowest price hours
price_and_demand['HOUR'] = price_and_demand.index.hour
negative_price = price_and_demand[price_and_demand['RRP'] < 0]
negative_price.plot(kind='bar', color='red', title='Average Hour of Negative Price')
negative_price = negative_price.groupby('HOUR')['RRP'].mean().sort_values(ascending=True)
print(f"the lowest-price hours is: {negative_price.head(1).index[0]} with average price of {round(negative_price.head(1).values[0], 2)} AUS/MWh")

# 2 plot the price in hour

price_and_demand.groupby('HOUR')['RRP'].mean().plot(kind='bar', color='blue', ylabel='Average Price (AUS/MWh)', title='Average Hour of Price')
# %%
