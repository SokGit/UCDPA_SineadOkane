#Step 1 Import Libararies for Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Sydney_HousePrices=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\FinalProject\SydneyHousePrices.csv')
#Reviwing Data with Head, tail and Describe.
print(Sydney_HousePrices.head(5))
print(Sydney_HousePrices.describe(include=['float','object']))





