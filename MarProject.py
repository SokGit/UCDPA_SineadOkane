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
#Use Orginal DF to get mean etc
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

Expensive_Houses['sellPrice'].plot(x='date',y='sellPrice',kind='line',color='r',xlabel=('Time(Years)'))

Below_AverageHouses['sellPrice'].plot()

#Too Much Data Given on above to acturately demonstrate findings

print(Sydney_HP.sellPrice.iloc[0:50])
#Import Datetime
from datetime import datetime, timedelta
Final_Dates_Sydney=datetime(2019,12,6)
print(Final_Dates_Sydney)

#Create a Sell Date for year before
Dates_Sydney_2018= Final_Dates_Sydney -timedelta(weeks=52)
print(Dates_Sydney_2018)
print((Sydney_HP.sellPrice.iloc[1000]))
print(Sydney_HP_ind2.sellPrice[0])

#Drop Duplicate Sell Prices to see range prices vs Property Type
Sydney_HP=Sydney_HP.drop_duplicates(subset='sellPrice')

#Reusable code for subsetting columns, dataframe and columns you wish to work with
# df['col_a','col_b']

#Suburb Castle Hill Area
CastleHill_Suburb=Sydney_HP[Sydney_HP['suburb']=='Castle Hill']
#Filter for rows where House price is less then average and Located in Castle Hill
BelowAverage_CastleHill= Sydney_HP[(Sydney_HP['sellPrice']<Mean)&(Sydney_HP['suburb']=='Castle Hill')&(Sydney_HP['propType']=='house')]
print(BelowAverage_CastleHill)
#Reuse Data above to input based on Townhouses and plot to axes
BelowAverage_CastleHillTH= Sydney_HP[(Sydney_HP['sellPrice']<Mean)&(Sydney_HP['suburb']=='Castle Hill')&(Sydney_HP['propType']=='townhouse')]
fig,ax=plt.subplots()
ax.plot(BelowAverage_CastleHill.index,BelowAverage_CastleHill['sellPrice'],color='green',linestyle='--',)
ax.set_xlabel('Date(Years)')
ax.set_ylabel('Price($500k-$1.2million)')
ax.set_title('Average cost of houses Castle Hill')


SydneyHP_Below300k=Sydney_HP[(Sydney_HP['sellPrice']<300000)&(Sydney_HP['propType']=='house')]
#Filter for rows where House price is less then 300k and Located in Castle Hill
BelowAverage_Castle_Hill= Sydney_HP[(Sydney_HP['sellPrice']<Mean)&(Sydney_HP['suburb']=='Castle Hill')&(Sydney_HP['propType']=='house')]

#Using Matplot Lib to create a line graph showing Rise and Fall of houses in Castle Hill Between 2013-2000
ax.plot(BelowAverage_Castle_Hill.index,BelowAverage_Castle_Hill['sellPrice'],color='green',linestyle='--')
ax.set_xlabel('Date(Years 2013-2020)')
ax.set_ylabel('Price(Range $93.4k-$125.2k)')
ax.set_title('Cost of houses Below Average Castle Hill(Sydney)')
plt.show()



#Zooming in over 5 years of Data between 2014-2019
Sydney_HP_Below300k=Sydney_HP.index.get_level_values('Date')
print(Sydney_HP_Below300k)
Sydney_HP_Below300k.tolist()
DecHP_2019=Sydney_HP_Below300k[0:10]
print(DecHP_2019)
import datetime as dt
start=Sydney_HP.index.searchsorted(dt.datetime(2019,12,31))
end=Sydney_HP.index.searchsorted(dt.datetime(2014,12,31))
SydneyOver5years=Sydney_HP.iloc[start:end]
print(SydneyOver5years)


#Getting Biggest range of Dates in 2019
Year_2019Data=Sydney_HP.loc['2019-12-06']

#Scenario Reset Index, using pandas to Drop the index colum from Date and reset to Suburbs
print(Sydney_HP.reset_index())
Sydney_suburb=Sydney_HP.set_index('suburb')
print(Sydney_suburb.columns)
#Cleaning Data by dropping columns Id,bed,bath,car not relevant for clients Dropping Columns
columns_to_drop=['Id','bed','bath','car']
Sydney_suburb=Sydney_suburb.drop(columns=columns_to_drop)
print(Sydney_suburb.head(10))
print(Sydney_suburb.columns)
print(Sydney_suburb.describe(include=['float','object']))
print(Sydney_suburb['postalCode'].value_counts())
#Sort By Highest Price First
Sydney_suburb=Sydney_suburb.sort_values('sellPrice',ascending=False)
print(Sydney_suburb.head())
#We have already estblashied the mean/standard dev of the Data above
#PropTypes subset to House below $300,000
SydneyHP_Below300k=Sydney_suburb[(Sydney_suburb['sellPrice']<300000)&(Sydney_suburb['propType']=='house')]
print(SydneyHP_Below300k.info())
print(SydneyHP_Below300k['postalCode'].value_counts())
print(SydneyHP_Below300k)
Suburbs_Below300k=Sydney_suburb.index.get_level_values('suburb')
print(Suburbs_Below300k)
Suburbs_Below300k.tolist()

#Make a list of Suburbs in Sydney
Suburbs_To_Keep=['Villawood','Eschol Park','Buxton','Tahmoor']
#Subset Suburbs Into Sydney Houses Price using square brackets to get a value in the Suburbs List
Suburbs_Requested=Sydney_suburb.loc[Suburbs_To_Keep]
print(Suburbs_Requested)
#Setting arrays on Suburbs with Villawood and Tahmoor
Suburbs_To_Keep_Array=np.array(['Villawood','Eschol Park','Buxton','Tahmoor'])
indexing_array=np.array([0,3])
Suburbs_Subset=Suburbs_To_Keep_Array[indexing_array]
print(Suburbs_Subset)


#Print(Sydney_HP.groupby('suburb')['sellPrice'].agg([mean]))
Sydney_suburb_stats=SydneyHP_Below300k.groupby('suburb')['sellPrice'].agg([np.mean])
print(Sydney_suburb_stats)

print(Below300k_Castle_Hill)























































