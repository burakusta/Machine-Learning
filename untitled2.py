# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:12:37 2024

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
df1["price"]=df1["price"].astype("float64")
sns.boxplot(x='drive-wheels', y="price", data=df1)



print(df1["drive-wheels"])
print(df1.info())
#drive_wheels_counts=(df1["drive-wheels"].value_counts()).to_frame()
#print(drive_wheels_counts)
#drive_wheels_counts=drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'})
#df1 = pd.concat([df1, drive_wheels_counts], axis=1)
#print(drive_wheels_counts)
#print(df1["drive_wheels_counts"])
