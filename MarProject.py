#Step 1 Import Libararies for Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Import The Data
Sydney_HP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv')
#Reviwing Data with Head,Describe and Info.
print(Sydney_HP.head(5))
print(Sydney_HP.describe(include=['float','object']))
#Based on data set Index to Date and Parse Date Columns as date so pandas knows its a date time series
Sydney_HP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv',parse_dates=['Date'],index_col='Date')
print(Sydney_HP.info())
print(Sydney_HP.shape)
print(Sydney_HP.values)
print(Sydney_HP.columns)
print(Sydney_HP.index)
#Sorting in ascending order.
print(Sydney_HP.sort_values('sellPrice'))
#Sorting by multiple variables
print(Sydney_HP.sort_values(['sellPrice','suburb']))
print(Sydney_HP['sellPrice'].mean())
print(Sydney_HP['sellPrice'].max())
#Subsetting based on Higher End of Market 2 Billion
HighMarket=Sydney_HP[Sydney_HP['sellPrice']>2000000000]
print(HighMarket)
#How Many Suburbs
print(Sydney_HP['suburb'].value_counts())
print(Sydney_HP.groupby('suburb')['sellPrice'].agg([max,min,sum]))
#Drop Duplicate Sell Prices&Call Sydney_Hp1, to see range prices vs Property Type
Sydney_Hp1=Sydney_HP.drop_duplicates(subset='sellPrice')
print(Sydney_Hp1)
#How Many Property Types in Sydney_Hp1
print(Sydney_Hp1['propType'].value_counts())
#Summaries by groups
Average_House=(Sydney_Hp1[Sydney_Hp1['propType']=='house']['sellPrice'].mean())
print(Average_House)
Average_Townhouse=(Sydney_Hp1[Sydney_Hp1['propType']=='townhouse']['sellPrice'].mean())
print(Average_Townhouse)
Average_Villa=(Sydney_Hp1[Sydney_Hp1['propType']=='villa']['sellPrice'].mean())
print(Average_Villa)
#Looping based on Propety SellPrice
x=Average_House
y=Average_Townhouse
if x>y:
    print('House_is_Greater')
else:
    print('Townhouse_is_Greater')
#Sorting in descending order
Sydney_Hp1.sort_values('Date',ascending=False)
print(Sydney_Hp1.groupby(['suburb','propType'])['sellPrice'].max())
Prices_Suburb_PropType=Sydney_Hp1.pivot_table(values='sellPrice',index='suburb',columns='propType')
print(Prices_Suburb_PropType)
#Returning to orginal as Droping Dup Values lost valuable data
#Decting any missing Values
print(Sydney_HP.isna().any())
#Based on above Missing Values in Bed and Car, find out how many and Fill with Zero
print(Sydney_HP.isna().sum())
Sydney_HP.fillna(0)
#Sort By Most Recent Date First
Sydney_HP=Sydney_HP.sort_values('Date',ascending=False)
print(Sydney_HP.head())
print(Sydney_HP.tail())
Mean=(Sydney_HP['sellPrice'].mean())
print(Mean)
Sydney_HP.sort_index()
print(Sydney_HP)
import datetime as dt
#Getting First Sell Price
print(Sydney_HP.sellPrice.iloc[0])
#Sorting by Multiple Values
Sydney_HP.sort_values(['Date','sellPrice'],ascending=[False,False])
print(Sydney_HP.head())
print(Sydney_HP['sellPrice'])
#Greater then the Mean
print(Sydney_HP['sellPrice'] >(Mean))
Sydney_GreaterAverage=Sydney_HP[Sydney_HP['sellPrice']>(Mean)]
#Standard Dev
print(Sydney_HP['sellPrice'].std())
Distance_From_Mean=(Sydney_HP['sellPrice'].mean()+Sydney_HP['sellPrice'].std())
print(Distance_From_Mean)
#Subsetting based on Houses
Sydney_Houses=Sydney_HP[Sydney_HP['propType']=='house']
#Subsetting based on Multiple Conditions
is_House=Sydney_HP['propType']=='house'
is_GreaterAverage=Sydney_HP['sellPrice']>1365000
print(Sydney_HP[is_House &is_GreaterAverage])
#Subsettingbased on higher End House
is_Highend=Sydney_HP['sellPrice']>(Distance_From_Mean)
print(Sydney_HP[is_House&is_Highend])
is_Below_Average=Sydney_HP['sellPrice']<(Mean)
print(Sydney_HP[is_House& is_Below_Average])
Expensive_Houses=Sydney_HP[is_House&is_Highend]
Below_AverageHouses=Sydney_HP[is_House& is_Below_Average]
fig, ax=plt.subplots()
print(Expensive_Houses['suburb'].value_counts())
print(Below_AverageHouses['suburb'].value_counts())
#Subsetting using.isin() For Expensive Houses(See what years more expensive to live in area)
is_RoseBay_or_Point_Piper=Expensive_Houses['suburb'].isin(['Rose Bay','Point Piper'])
print(is_RoseBay_or_Point_Piper)
Sydney_HP_ind2=Sydney_HP.set_index('suburb')
print(Sydney_HP_ind2.head())
Sydney_HP_ind2=Sydney_HP_ind2.sort_values('sellPrice',ascending=False)
print(Sydney_HP_ind2.head())
#Ploting Data, we have imported Matplotlib previously
#Subsetting based on Houses
Sydney_Houses=Sydney_HP[Sydney_HP['propType']=='house']
Sydney_Houses['sellPrice'].plot(x='date',y='sellPrice',kind='line')
plt.show()
Expensive_Houses['sellPrice'].plot(x='date',y='sellPrice',kind='line',color='r',xlabel=('Time(Years)'))
plt.show()
Below_AverageHouses['sellPrice'].plot()
plt.show()
#Above Too Much Data Given on above to acturately manipulate
#2nd Data Set
Perth_Houses=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\PerthHousePrices.csv',parse_dates=['DATE_SOLD'],index_col=['DATE_SOLD'])
print(Perth_Houses.head())
print(Perth_Houses.info())

print(Sydney_HP.sellPrice.iloc[0:50])

from datetime import datetime, timedelta
Final_Dates_Sydney=datetime(2019,12,6)
print(Final_Dates_Sydney)

#Create a Sell Date for year before
Dates_Sydney_2018= Final_Dates_Sydney -timedelta(weeks=52)
print(Dates_Sydney_2018)
print((Sydney_HP.sellPrice.iloc[1000]))
print(Sydney_HP_ind2.sellPrice[0])

#Reusable code for subsetting columns, dataframe and columns you wish to work with
# df['col_a','col_b']

#Suburb Castle Hill Area
CastleHill_Suburb=Sydney_HP[Sydney_HP['suburb']=='Castle Hill']
#Filter for rows where House price is less then average and Located in Castle Hill
BelowAverage_CastleHill= Sydney_HP[(Sydney_HP['sellPrice']<Mean)&(Sydney_HP['suburb']=='Castle Hill')&(Sydney_HP['propType']=='house')]
print(BelowAverage_CastleHill)
#Reuse Data above to input based on Townhouses and plot to axes
fig,ax=plt.subplots()
ax.plot(BelowAverage_CastleHill.index,BelowAverage_CastleHill['sellPrice'],color='green',linestyle='--',)
ax.set_xlabel('Date(Years)')
ax.set_ylabel('Price($500k-$1.2million)')
ax.set_title('Average cost of houses Castle Hill')
plt.show()

#Getting Biggest range of Dates in 2019
Year_2019Data=Sydney_HP.loc['2019-12-06']






































