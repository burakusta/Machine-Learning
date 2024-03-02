# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:44:05 2024

@author: burak
"""
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
#filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
#df = pd.read_csv(filepath, header=None)
#headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body-style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
#df.columns=headers
df1=df.replace('?',np.NaN)
df1["price"]=df1["price"].astype("float64")
df1["horsepower"]=df1["horsepower"].astype("float64")
#print("buradayımmm",df1["horsepower"].astype("float64"))
print("burada ne varrrrrrr\n",df1["horsepower"])
for_mean=(df1['horsepower'].mean(skipna=True))
df1['horsepower']=df1['horsepower'].replace(np.NaN,for_mean)
print("burada ne varrrrrrr\n",df1["price"])


#print(df1["drive-wheels"])
drive_wheels_counts=(df1["drive-wheels"].value_counts()).to_frame()
drive_wheels_counts=drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'})
drive_wheels_counts.index.name = 'drive-wheels'
#print(drive_wheels_counts)
h=sns.boxplot(x='engine-location', y="price", data=df1)
plt.show(h)
engine_location_counts=(df1["engine-location"].value_counts()).to_frame()
#print(engine_location_counts)
df1["engine-size"]=df1["engine-size"].astype("float64")
x=df1["engine-size"]
y=df1["price"]
a=plt.scatter(x, y)
plt.show(a)
b=sns.regplot(x,y)
plt.show(b)
#print(df1["price"].dtypes,df1['price'].unique())
df_group_one = df1[['drive-wheels','body-style','price']]
df_group_test = df_group_one.groupby(['drive-wheels','body-style'],as_index=False).mean()
#print(df_group_test)
grouped_pivot = df_group_test.pivot(index='drive-wheels',columns='body-style')
#print(grouped_pivot)
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()
#c=plt.pcolor(grouped_pivot, cmap='RdBu')
#plt.colorbar()
#plt.show(c)
print(df1['body-style'].unique())
print("burada ne varrrrrrr\n",df1["price"])
print("burada ne varrrrrrr\n",df1["horsepower"])
pearson_coef, p_value = stats.pearsonr(df1['horsepower'], df1['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  
#print(drive_wheels_counts)
#print(df1["drive_wheels_counts"])