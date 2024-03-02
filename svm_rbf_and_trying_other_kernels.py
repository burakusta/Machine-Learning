# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:13:07 2024

@author: burak
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,classification_report,f1_score,jaccard_score
from sklearn.model_selection import train_test_split
from sklearn import metrics,preprocessing
from sklearn import svm
path=r"C:\Users\burak\OneDrive\Masaüstü\datas\cell_samples.csv"
cell_df = pd.read_csv(path, header=0)
#cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'], errors='coerce').notnull()]   ???????????
cell_df['BareNuc']=cell_df['BareNuc'].replace('?',np.NaN)
cell_df=cell_df.dropna(subset=['BareNuc'], axis=0)
cell_df['BareNuc'] = cell_df['BareNuc'].astype('int')
feature_df = cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
X = np.asarray(feature_df)
y = np.asarray(cell_df['Class'])
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
clf = svm.SVC(kernel='rbf')
clf.fit(X_train, y_train) 
yhat = clf.predict(X_test)
# plot_confusion_matrix ???
'''def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')'''
f1score1=f1_score(y_test, yhat, average='weighted') 
jaccard1=jaccard_score(y_test, yhat,pos_label=2)
clf2 = svm.SVC(kernel='linear')
clf2.fit(X_train, y_train) 
yhat2 = clf2.predict(X_test)
f1score2=f1_score(y_test, yhat2,pos_label=2) 
jaccard2=jaccard_score(y_test, yhat2,pos_label=2)


