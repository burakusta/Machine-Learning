# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:08:45 2024

@author: burak
"""

from sklearn.linear_model import LinearRegression
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load the dataset
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)

# Create a linear regression model
lm = LinearRegression()
lm1 = LinearRegression()

# Select features and target variable
x = df[['engine-size']]
x1 = df['highway-mpg']
y = df['price']

# Fit the model
lm.fit(x, y)

# Predict the target variable
y_new = lm.predict(x.values)
y_new1=lm.coef_*x+lm.intercept_

# Plotting the original data and the fitted line

plt.scatter(x, y, color='blue', label='Original Data')
#plt.plot(x.values, y_new, color='red', label='Fitted Line')
plt.plot(x.values, y_new1.values, color='red', label='Fitted Line')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.title('Linear Regression: Engine Size vs Price')
plt.legend()
plt.show()


sns.residplot(x, y,data=df)
plt.show()

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm1.fit(Z, df['price'])
Y_hat_new=lm1.coef_[0]*df['horsepower']+lm1.coef_[1]*df['curb-weight']+lm1.coef_[2]*df['engine-size']+lm1.coef_[3]*df['highway-mpg']+lm1.intercept_
Y_hat = lm1.predict(Z)
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat_new.values, hist=False, color="b", label="Fitted Values" , ax=ax1)
plt.show()


#f = np.polyfit(x1, y, 3)
#p = np.poly1d(f)
#y_new2=p(x1)
#plt.scatter(x1, y_new2, color='red')
#plt.scatter(x1, y, color='blue')
#plt.show()
#pr=PolynomialFeatures(degree=2)
#=pr.fit_transform(df[['horsepower', 'curb-weight']])
#print("\n",x_polly,"\n")
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(Z,y)
ypipe=pipe.predict(Z)
ax2 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(ypipe, hist=False, color="b", label="Fitted Values" , ax=ax2)
plt.show()
#print(p)
#print(f)