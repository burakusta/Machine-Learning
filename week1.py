# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:39:37 2024

@author: burak
"""

import pandas as pd
import numpy as np
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path,header=0)
filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
df1 = pd.read_csv(filepath, header=None)
headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb- weight","engine-type", "num-of-cylinders", "engine-size","fuel- system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway- mpg","price"]
df1.columns=headers
df1=df1.replace('?',np.NaN)
df1=df1.dropna(subset=["price"], axis=0)
df1=df1.dropna(subset=['normalized-losses'], axis=0)
print(df)
print(df.tail(3))



