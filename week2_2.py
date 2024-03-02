# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:49:05 2024

@author: burak
"""

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
path=r"C:\Users\burak\OneDrive\Masaüstü\datas\FuelConsumption.csv"
df = pd.read_csv(path, header=0)
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
viz.hist()
plt.show()
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='black')
plt.show()
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
regr = linear_model.LinearRegression()
#train_x = np.asanyarray(train[['ENGINESIZE']])
#train_y = np.asanyarray(train[['CO2EMISSIONS']])
x_train=train[["ENGINESIZE"]]
y_train=train["CO2EMISSIONS"]
regr.fit(x_train, y_train)
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train[["ENGINESIZE"]].values, regr.coef_[0]*train[["ENGINESIZE"]].values + regr.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
test_y_=regr.predict(test[["ENGINESIZE"]])
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test["CO2EMISSIONS"])))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test["CO2EMISSIONS"]) ** 2))
print("R2-score: %.2f" % r2_score(test["CO2EMISSIONS"] , test_y_) )
cdf2 = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
msk2 = np.random.rand(len(df)) < 0.8
train2 = cdf2[msk2]
test2 = cdf2[~msk2]
regr2 = linear_model.LinearRegression()
#x = np.asanyarray(train2[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']])
#y = np.asanyarray(train2[['CO2EMISSIONS']])
x_train2=train2[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']]
y_train2=train2['CO2EMISSIONS']
x_test2=test2[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB']]
regr2.fit(x_train2, y_train2)
y_test2=test2['CO2EMISSIONS']
plt.show()
y_hat= regr2.predict(x_test2)
print("Mean Squared Error (MSE) : %.2f"
      % np.mean((y_hat - y_test2) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr2.score(x_test2, y_test2))
