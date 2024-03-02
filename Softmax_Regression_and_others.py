# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 20:56:54 2024

@author: burak
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,classification_report,f1_score,jaccard_score,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing
from sklearn import svm,datasets
pair=[1, 3]
iris = datasets.load_iris()
X = iris.data[:, pair]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu) #c=y'yi anlamadım, bakıcam
plt.xlabel("sepal width (cm)")
plt.ylabel("petal width")
lr = LogisticRegression(random_state=0).fit(X_train, y_train)
probability=lr.predict_proba(X_test)
'''def plot_probability_array(X,probability_array):

    plot_array=np.zeros((X.shape[0],30))
    col_start=0
    ones=np.ones((X.shape[0],30))
    for class_,col_end in enumerate([10,20,30]):
        plot_array[:,col_start:col_end]= np.repeat(probability_array[:,class_].reshape(-1,1), 10,axis=1)
        col_start=col_end
    plt.imshow(plot_array)
    plt.xticks([])
    plt.ylabel("samples")
    plt.xlabel("probability of 3 classes")
    plt.colorbar()
    plt.show()'''
#plot_probability_array(X,probability)

