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
X = df[['region', 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] 
y = df['custcat'].values
#X = preprocessing.StandardScaler().fit(X).transform(X.astype(float)) #??????????
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4) #????????

k = 4
#Train Model and Predict  
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
yhat = neigh.predict(X_test)
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))

#K1
mylist=np.ones(10)
mylist2=np.ones(10)
# for i in range(1,10): ####şuna tekrar bak, hata var!
#     neigh = KNeighborsClassifier(n_neighbors = i).fit(X_train,y_train)
#     yhat = neigh.predict(X_test)
#     mylist[i-1]=metrics.accuracy_score(y_train, neigh.predict(X_train))
#     mylist2[i]=metrics.accuracy_score(y_test, yhat)
# y=mylist
# #x=np.range(1, len(mylist))
# plt.plot(range(1, len(mylist)),y)
# plt.show()
