# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:26:40 2024

@author: burak
"""
import seaborn as sns
import pandas as pd
import numpy as np
filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
df = pd.read_csv(filepath, header=None)
headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
df.columns=headers
df1=df.replace('?',np.NaN)
print(df1["drive-wheels"].value_counts())
print(df1["drive-wheels"])
#df1['drive-wheels'].value_counts().to_frame()
headers= ["deneme","value count"]
#my_try=pd.DataFrame(df1["drive-wheels"].value_counts())
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
print("burası\n",drive_wheels_counts)
drive_wheels_counts=drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'})
print("burasıı\n",drive_wheels_counts)
drive_wheels_counts.index.name = 'drive-wheels'
print(drive_wheels_counts)
sns.boxplot(x="drive_wheels", y="price", data=df)
#print(df[['bore', 'stroke','horsepower']].corr())
#df1['drive-wheels'].value_counts().columns=headers
#print(my_try)
#print(df1["drive-wheels"].value_counts())

#df1["drive-wheels"]=df1["drive-wheels"].rename(columns={})