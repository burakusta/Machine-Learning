# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:02:33 2024

@author: burak
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df1= pd.read_csv(path)
df1["price"]=df1["price"].astype(dtype=float)
df1["horsepower"]=df1["horsepower"].astype(dtype=float)
df1["bore"]=df1["bore"].astype(dtype=float)
df1["stroke"]=df1["stroke"].astype(dtype=float)
myy=df1[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()
sns.regplot(x="engine-size", y="price", data=df1)
plt.show()
myy2=df1[["engine-size", "price"]].corr()
sns.boxplot(x="engine-size", y="price", data=df1)
plt.show()
df_group_one = df1[['drive-wheels','body-style','price']]
grouped_test1 = df_group_one.groupby(['drive-wheels','body-style'],as_index=False).mean()
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
pearson_coef, p_value = stats.pearsonr(df1['wheel-base'], df1['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)
