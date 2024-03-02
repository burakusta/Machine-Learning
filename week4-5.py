# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:49:07 2024

@author: burak
"""

from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score,cross_val_predict
from sklearn.linear_model import Ridge
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df1 = pd.read_csv(path,header=0)
#filepath=r"C:\Users\burak\OneDrive\Masaüstü\auto.csv"
#df1 = pd.read_csv(filepath, header=None)
#headers = ["symboling","normalized-losses","make", "fuel-type","aspiration", "num-of-doors","body- style", "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type", "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highway-mpg","price"]
#df1.columns=headers
df1=df1.replace('?',np.NaN)
df1["curb-weight"]=df1["curb-weight"].astype(dtype=float)
df1["horsepower"]=df1["horsepower"].astype(dtype=float)
df1['engine-size']=df1['engine-size'].astype(dtype=float)
df1['highway-mpg']=df1['highway-mpg'].astype(dtype=float)
lm = LinearRegression()
X = df1[['highway-mpg']]
Y = df1['price']
lm.fit(X,Y)
Yhat=lm.predict(X)
print("here",lm.intercept_,lm.coef_)
#Z = df1[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
#lm.fit(Z, df1['price'])
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df1)
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df1['highway-mpg'], y=df1['price'])
plt.show()
#Y_hat = lm.predict(Z)
x = df1['highway-mpg']
y = df1['price']
pr=PolynomialFeatures(degree=2)
#Z_pr=pr.fit_transform(Z)
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
#Z = Z.astype(float)
#pipe.fit(Z,y)
#ypipe=pipe.predict(Z)
print('The R-square is: ', lm.score(X, Y))
mse = mean_squared_error(df1['price'], Yhat)
print('The mean square error of price and predicted value is: ', mse)


y_data = df1['price']
x_data=df1.drop('price',axis=1)
lre=LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
lre.fit(x_train[['horsepower']], y_train)
num1=lre.score(x_test[['horsepower']], y_test)
num2=lre.score(x_train[['horsepower']], y_train)
Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4).mean()
yhat = cross_val_predict(lre,x_data[['horsepower']], y_data,cv=4)

lr = LinearRegression()
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])


pr5 = PolynomialFeatures(degree=2)
x_train_pr = pr5.fit_transform(x_train[['horsepower']])
x_test_pr = pr5.fit_transform(x_test[['horsepower']])
poly = LinearRegression()
poly.fit(x_train_pr, y_train)
yhat2 = poly.predict(x_test_pr)


pr2=PolynomialFeatures(degree=2)
x_train_pr1=pr2.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr1=pr2.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
RigeModel=Ridge(alpha=1)
RigeModel.fit(x_train_pr, y_train)
yhat3 = RigeModel.predict(x_test_pr)