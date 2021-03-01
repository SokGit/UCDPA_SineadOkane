#Step 1 Import Libararies for Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Sydney_HP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv')
#Reviwing Data with Head,Describe and Info.
print(Sydney_HP.head(5))
print(Sydney_HP.describe(include=['float','object']))
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
print(Sydney_HP.groupby('suburb')['sellPrice'].agg([max]))
#Drop Duplicate Sell Prices&Call Sydney_Hp1
Sydney_Hp1=Sydney_HP.drop_duplicates(subset='sellPrice')
print(Sydney_Hp1)
#How Many Property Types in Sydney_Hp1
print(Sydney_Hp1['propType'].value_counts())
#Summaries by groups
print(Sydney_Hp1[Sydney_Hp1['propType']=='house']['sellPrice'].mean())
print(Sydney_Hp1[Sydney_Hp1['propType']=='townhouse']['sellPrice'].mean())
print(Sydney_Hp1[Sydney_Hp1['propType']=='villa']['sellPrice'].mean())









