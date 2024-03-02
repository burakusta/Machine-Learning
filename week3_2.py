# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:55:51 2024

@author: burak
"""

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
path=r"C:\Users\burak\OneDrive\Masaüstü\datas\teleCust1000t.csv"
df = pd.read_csv(path, header=0)
#df.hist(column='income', bins=50)
X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values
y = df['custcat'].values
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float)) #??????????
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.001, random_state=4) #????????

k = 4
#Train Model and Predict  
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat = neigh.predict(X_test)
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
#print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
x_try=df[["age"]]
y_try=[df["income"]]
plt.scatter(x_try,y_try)
plt.show()
K=1
mylist=np.ones(20)
mylist2=np.ones(20)
for i in range(20):
    neigh = KNeighborsClassifier(n_neighbors = i+1).fit(X_train,y_train)
    yhat = neigh.predict(X_test)
    mylist[i]=metrics.accuracy_score(y_train, neigh.predict(X_train))
    mylist2[i]=metrics.accuracy_score(y_test, yhat)
y=mylist
x=np.arange(1, len(mylist)+1)
plt.plot(x,y)
plt.show()