# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:31:41 2024

@author: burak
"""

import pandas as pd
import numpy as np
filepath=r"C:\Users\burak\OneDrive\Masaüstü\datas\cars.csv"
headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
df1 = pd.read_csv(filepath, header=0)
df1.columns=headers
df1.replace("?", np.nan, inplace = True)
df1["price"]=df1["price"].astype(dtype=float)
df1["horsepower"]=df1["horsepower"].astype(dtype=float)
missing_data = df1["price"].isnull().sum()
avg_price = df1["price"].mean()
df1["price"]=df1["price"].replace(np.nan, avg_price)
print(df1['num-of-doors'].value_counts())
print("en çok tekrar eden değer",df1['num-of-doors'].value_counts().idxmax())
df1['city-L/100km'] = 235/df1["city-mpg"]
bins = np.linspace(min(df1["horsepower"]), max(df1["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df1['horsepower-binned'] = pd.cut(df1['horsepower'], bins, labels=group_names, include_lowest=True )
dummy_variable = pd.get_dummies(df1["fuel-type"])
df1 = pd.concat([df1, dummy_variable], axis=1)