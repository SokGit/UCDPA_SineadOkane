#Step 1 Import Libararies for Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Import The Data #Reusable code df=pd.read_csv(),
Sydney_HP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv')
#Reviwing Data with Head,Describe
print(Sydney_HP.head(5))
print(Sydney_HP.describe(include=['float','object']))
#Based on data set Index to Date and Parse Date Columns as date so pandas knows its a date time series
Sydney_HP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv',parse_dates=['Date'],index_col='Date')
#Inspecting the Data.
print(Sydney_HP.info())
print(Sydney_HP.shape)
print(Sydney_HP.values)
print(Sydney_HP.columns)
print(Sydney_HP.index)
#Sorting in ascending order.#resulable code df.sort_values('column')
print(Sydney_HP.sort_values('sellPrice'))
#Sorting by multiple variables
print(Sydney_HP.sort_values(['sellPrice','suburb']))
print(Sydney_HP['sellPrice'].mean())
print(Sydney_HP['sellPrice'].max())
#Subsetting based on Higher End of Market 2 Billion
HighMarket=Sydney_HP[Sydney_HP['sellPrice']>2000000000]
print(HighMarket)
#How Many enteries per suburb Suburbs#resuable code df['column'].value_counts()
print(Sydney_HP['suburb'].value_counts())
#Using the .groupby.and .agg method in pandas.
print(Sydney_HP.groupby('suburb')['sellPrice'].agg([max,min,sum]))
#Drop Duplicate Sell Prices&Call Sydney_Hp1, to see range prices vs Property Type#reusable code df.drop_duplicates(subset='column')
Sydney_Hp1=Sydney_HP.drop_duplicates(subset='sellPrice')
print(Sydney_Hp1)
#How Many Property Types in Sydney_Hp1#Reusing code above from suburbs
print(Sydney_Hp1['propType'].value_counts())
#Summaries by groups #reuable code df[df['column']=='data in column selected']
Average_House=(Sydney_Hp1[Sydney_Hp1['propType']=='house']['sellPrice'].mean())
print(Average_House)
Average_Townhouse=(Sydney_Hp1[Sydney_Hp1['propType']=='townhouse']['sellPrice'].mean())
print(Average_Townhouse)
Average_Villa=(Sydney_Hp1[Sydney_Hp1['propType']=='villa']['sellPrice'].mean())
print(Average_Villa)
#If statements based on Propety SellPrice
x=Average_House
y=Average_Townhouse
if x>y:
    print('House_is_Greater')
else:
    print('Townhouse_is_Greater')
#Sorting in descending order, highest date first.
Sydney_Hp1.sort_values('Date',ascending=False)
print(Sydney_Hp1.groupby(['suburb','propType'])['sellPrice'].max())
Prices_Suburb_PropType=Sydney_Hp1.pivot_table(values='sellPrice',index='suburb',columns='propType')
print(Prices_Suburb_PropType)
#Use Orginal DF to get mean etc
#Decting any missing Values#re usable code df.isna().any()
print(Sydney_HP.isna().any())
#Based on above Missing Values in Bed and Car, find out how many and Fill with Zero
print(Sydney_HP.isna().sum())
Sydney_HP.fillna(0)#re usbale code df.fillna()
#Sort By Most Recent Date First
Sydney_HP=Sydney_HP.sort_values('Date',ascending=False)
print(Sydney_HP.head())
print(Sydney_HP.tail()) #re usbale code df.tail()
Mean=(Sydney_HP['sellPrice'].mean())
print(Mean)
Sydney_HP.sort_index()
print(Sydney_HP)
import datetime as dt
#Getting First Sell Price
print(Sydney_HP.sellPrice.iloc[0])
#Sorting by Multiple Values, highest date and highest price
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
#Subsetting based on higher End House
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
#Set suburb as index#re suable code df.set_index('column name')
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
#LOC&ILOC Recommended for larger datasets
print(Sydney_HP.sellPrice.iloc[0:50])
#Find price last day of dec 2019
print(Sydney_HP.loc['2019-12-31','sellPrice'])

#Basic Building Block:Pd timestamp
from datetime import datetime
time_stamp=pd.Timestamp(datetime(2019,12,2))
pd.Timestamp('2019-01-01')==time_stamp

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
# From above to be used for plotting Filter for rows where House price is less then average and Located in Castle Hill
BelowAverage_Castle_Hill= Sydney_HP[(Sydney_HP['sellPrice']<Mean)&(Sydney_HP['suburb']=='Castle Hill')&(Sydney_HP['propType']=='house')]

#Using Matplot Lib to create a line graph showing Rise and Fall of houses in Castle Hill Between 2013-2000
ax.plot(BelowAverage_Castle_Hill.index,BelowAverage_Castle_Hill['sellPrice'],color='green',linestyle='--')
ax.set_xlabel('Date(Years 2013-2020)')
ax.set_ylabel('Price(Range $934k-$1.25million)')
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
print(Sydney_HP.reset_index())#resuable code df.reset_index()
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
Suburbs_Below300k.tolist() #resubale code df.tolist()

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



#Import the data and replace 'n/a' with np.nan, set index to date
Perth=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\All_Perth.csv',na_values='n/a',parse_dates=['DATE_SOLD'])
#Inspect table structure&data types
print(Perth.info())

#re usable code .rename(columns={old_name: new_name}).Preparing Data to be merged.

Perth=Perth.rename(columns={'SUBURB':'suburb'})
Perth=Perth.rename(columns={'PRICE':'sellPrice'})
Perth=Perth.rename(columns={'BEDROOM':'bed'})
Perth=Perth.rename(columns={'DATE_SOLD':'Date'})
print(Perth.sort_values('sellPrice'))
Perth=Perth.drop_duplicates(subset='sellPrice')
#Sorting on House Prices alone
Sydney_HP=Sydney_HP[(Sydney_HP['propType']=='house')]

#Add City Reference Columns to find which city is which.
Perth['City']='PERTH'
Sydney_HP['City']='SYDNEY'
Cities=['PERTH','SYDNEY']
# Create an empty list: Australia for looping
Australia=[]

#Concatenate DataFrames, Perth and Sydney_HP from earlier
Australia_HP=pd.concat([Perth,Sydney_HP])
print(Australia_HP.info())

#Sorting the years between 2000 and 2020
Australia_HP2000_2020=Australia_HP[(Australia_HP['Date']=='2000:2004')&(Australia_HP['Date']=='2005:2009')&(Australia_HP['Date']=='2010:2014')&(Australia_HP['Date']=='2015:2020')]




#Mean
Sydney_Mean=(Sydney_HP['sellPrice'].mean())
Perth_Mean=(Perth['sellPrice'].mean())
print(Sydney_Mean)
print(Perth_Mean)
Sydney_Price=Sydney_HP['sellPrice']
Sydney_Price.tolist()
print(Sydney_Price)
Perth_Price=Perth['sellPrice']
Perth_Price.tolist()
print(Perth_Price)
#If statement based on max Price
PerthMax=(Perth_Price.max())
SydneyMax=(Sydney_Price.max())
x=PerthMax
y=SydneyMax

if x>y:
    print('Perth More Expensive')
else:
    print('Sydney More Expensive')

#We learn sydney overall is more expensive
from datetime import datetime
datetime_object=datetime.now()
print(datetime_object)
my_string='2018-09-01'
my_date=datetime.strptime(my_string,"%Y-%m-%d")
print(my_date)
print('Type: ',type(my_date))
Year=('Year: ', my_date.year)

#Setting Date to read only Year

Australia_HP['Date']=pd.to_datetime(Australia_HP['Date'])
Australia_HP['Date']=Australia_HP['Date'].dt.year
print(Australia_HP['Date'])
Australia_HPMean=Australia_HP['sellPrice'].mean()

Australia_HP=Australia_HP.set_index('Date')
Australia_HP.dropna() #Reusable code df.dropna()
print(Australia_HP.head(5))
print(Australia_HPMean)
print(Australia_HP.columns)
#House prices below 800k
AustraliaHP_Overtheyears=Australia_HP[(Australia_HP['sellPrice']<800000)]
fig,ax=plt.subplots()
print(AustraliaHP_Overtheyears)
print(AustraliaHP_Overtheyears['suburb'].value_counts())
ax.bar(AustraliaHP_Overtheyears.index,AustraliaHP_Overtheyears['sellPrice'])
ax.set_xlabel('Years 1990-2020(5 year range)')
ax.set_ylabel('Price(Range $100k-$800k)')
ax.set_title('Rise of houses Price in Australia over the years')
plt.xticks(rotation=45)
plt.show()

#Iterate over rows with Dict dataframe in pandas
#Using Subsetted CastleHill
BelowAverage_CastleHillHead=BelowAverage_CastleHill.head(5)
#Index(Date),SellPrice and PropType
df=BelowAverage_CastleHillHead
for i, row in df.iterrows():
   print(i, row[3],row[7])
#Using First Five Rows to indicate prices below Average in different months in 2019
for index, row in BelowAverage_CastleHillHead.iterrows():
    print(index,':',row['suburb'], 'costs', row['sellPrice'], 'to buy a',row['bed'],'bedroom house in Castlehill in Syndey')
#Inspect summary stats (Divide by 1000 to get in K's)
Australia_HP1=Australia_HP['sellPrice']//1000
print(Australia_HP1.describe())
#Using Numpy.arange for steps #re usable code(np.arange(start=,stop=,step=)#Better example presented below
Quantiles=np.arange(start=.20,stop=.80,step=.20)
Deciles=Australia_HP['sellPrice'].quantile(Quantiles)
Deciles.plot(kind='barh',title='Australia Houses Prices Percentages')

#Sorting values by sell Price
Australia_HP.sort_values('sellPrice',ascending=False,inplace=True)
Australia_HPSuburbs=Australia_HP['suburb'].unique() #Reusable code df['column'].unique()
#Using Dict list and numpy to get the top 5 Most expensive Suburb in Australia,
Top5MostExpensive=Australia_HPSuburbs[0:5]
print(Top5MostExpensive)
#House prices in middle
print(Australia_HPSuburbs[400:407])
#Using numpy to get first row
Largest_Australia=Australia_HP.iloc[0]
Lowest_Australia=Australia_HP.iloc[-1]
print(Largest_Australia)
print(Lowest_Australia)


import seaborn as sns
import matplotlib.pyplot as plt

#Using Boolan True or False to see if perth in columns
print(Australia_HP['City']=='PERTH')

#Filter out prices above the 75th percentile with Australia_Hp1
Australia_HP1= Australia_HP1[Australia_HP1<Australia_HP1.quantile(.75)]
ax=sns.displot(Australia_HP1)
plt.show()
print(Australia_HP['suburb'].value_counts())#We learn that Gregory Hills has the most enteries
#Re usable code df['column name'].value_counts()(to get how many enteriest for element within that sector)

#Now that we have gotten information of sell prices over the years lets subsut to six most expensive in both cities(Sydney and Perth), putting Highest price first
Perth.sort_values('sellPrice',ascending=False,inplace=True)
Sydney_HP.sort_values('sellPrice',ascending=False,inplace=True)
#Using .head to get the top 3 most expensive suburbs in both cities.
Perth_H=Perth.head(3)
Sydney_H=Sydney_HP.head(3)
Australia_HP=pd.concat([Perth_H,Sydney_H])


#Grouping Data by Suburb displaying better by dividing by 1000 to present data more accurately
Australia_HP['sellPrice_m']=Australia_HP['sellPrice'].div(1e3)
#No longer need sellPrice as have 'sellPrice_m, axis=1 to let its a columns to be dropped displaying
Australia_HP=Australia_HP.drop('sellPrice',axis=1)
#Grouping by suburb using .groupby() and Looping Data to get the mean sellPrice in each suburb using pandas
Australia_by_suburb=Australia_HP.groupby('suburb')
for suburb,data in Australia_by_suburb:
    print(suburb,data.sellPrice_m.mean())
#Next Skip the loop
Mean_MostExpensive=Australia_by_suburb.sellPrice_m.max()
title='Average Price of Top Six Expensive Suburbs'
xlabel='Suburbs'
ylabel='(Average Price in K(OOOs)$)'
Mean_MostExpensive.plot(kind='bar',xlabel=xlabel,ylabel=ylabel,title=title)
plt.xticks(rotation=45)
plt.show()

#Using Numpy.arange for steps #re usable code(np.arange(start=,stop=,step=)
Quantiles=np.arange(start=.10,stop=.99,step=.10)
Deciles=Australia_HP['sellPrice_m'].quantile(Quantiles)
Deciles.plot(kind='barh',title='Australia Houses Prices Percentages',color='green')
plt.xticks(rotation=45)
plt.ylabel('(Percentages steps of 10%)')
plt.xlabel('(Price in K(000s) $)')
plt.show()





