import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r'c:\Users\jjbcs\Desktop\IBI\IBI_2024-25\IBI1_2024-25\Practical10')
# os.getcwd()
# os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# dalys_data.head(5)
# print(dalys_data.info())
dalys_data.describe()
max = dalys_data['DALYs'].max()
min = dalys_data['DALYs'].min()
print(f"Max: {max}, Min: {min}")
first = dalys_data['Year'].min()
last = dalys_data['Year'].max()
print(f"First year: {first}, Last year: {last}")

print(dalys_data.iloc[0:10,2])
#he 10th year for which DALYs were recorded in Afghanistan is 1999

#read just the “Year” column, but all the rows from dalys_data
print(dalys_data.loc[:,"Year"])
#create a Boolean that is True when the “Year” is “1990”, but false otherwise
year_1990 = dalys_data["Year"] == 1990
#find exactly the rows 
print(dalys_data.loc[year_1990,:])


uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
fr = dalys_data.loc[dalys_data.Entity=="France", ["DALYs", "Year"]]
uk_mean = uk["DALYs"].mean()
fr_mean = fr["DALYs"].mean()
if uk_mean > fr_mean:
    print("UK has a higher mean DALYs than France")
elif uk_mean < fr_mean:   
    print("France has a higher mean DALYs than UK") 
else:   
    print("UK and France have the same mean DALYs")
#UK has a higher mean DALYs than France
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in the UK")
plt.show()

# What country or countries have recorded a DALYs greater than 650,000 in a single year?
DALYs_650000 = dalys_data[dalys_data["DALYs"] > 650000]
contries = DALYs_650000["Entity"].unique()
print(f"Countries with DALYs greater than 650,000: {contries}") # only Rwanda
