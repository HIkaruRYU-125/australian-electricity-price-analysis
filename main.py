#%%
# import modules
import pandas as pd
import matplotlib.pyplot as plt


#%%
# This part ís the introduction of the program and the input of the csv file
print("This program will help you to analyze the negative price in AEMO's NEM Price and demand data.")
print("Please make sure the csv file is available and has the following columns: SETTLEMENTDATE, RRP, DEMAND")
try:
    file = input("Please input a NEM's Price and demand csv file name: ")
    price_and_demand = pd.read_csv(file, index_col= 'SETTLEMENTDATE', parse_dates=True)
except FileNotFoundError:
    print("The specified file was not found. Please check the file name and try again.")
    exit()
if price_and_demand.empty:
    print("The csv file is empty. Please check the file and try again.")
    exit()
if not all(col in price_and_demand.columns for col in ['RRP', 'TOTALDEMAND']):
    print("The csv file does not have the required columns. Please check the file and try again.")
    exit()
print(price_and_demand)

#%%
# This part of the code is to confirm the period of the data
Start_date = price_and_demand.index.min().strftime('%Y-%m-%d %H:%M:%S')
End_date = price_and_demand.index.max().strftime('%Y-%m-%d %H:%M:%S')
print(f"This data is observed from {Start_date} to {End_date}")
#%%
# select action option
# extracting hours
price_and_demand['HOUR'] = price_and_demand.index.hour
# filtering negative price and group by hour
negative_price = price_and_demand[price_and_demand['RRP'] < 0]

if negative_price.empty: #in case there is no negative price in the data
    print("There is no negative price in the data.")
    exit()
else: # reporting and plotting negative values
    negative_price = negative_price.groupby('HOUR')['RRP'].mean().sort_values(ascending=True)
    lowest_hour = negative_price.head(1).index[0]
    lowest_value = round(negative_price.head(1).values[0], 2)
    print(f"the lowest-price hours is: {lowest_hour}:00 with average price of {lowest_value} AUS/MWh")
    negative_price.plot(kind='bar', color='red', edgecolor='black')
    plt.title('Average Hour of Negative Price')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Price (AUD/MWh)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# 2 plot the overall price in hour (all price included)
price_and_demand.groupby('HOUR')['RRP'].mean().plot(kind='bar', color='blue', edgecolor='black')
plt.ylabel('Average Price (AUS/MWh)')
plt.title('Average Hour of Price')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# %%
