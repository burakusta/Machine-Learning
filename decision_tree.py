# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 20:56:09 2024

@author: burak
"""

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics,preprocessing
import sklearn.tree as tree
from sklearn.tree import DecisionTreeClassifier
path=r"C:\Users\burak\OneDrive\Masaüstü\datas\drug200.csv"
my_data = pd.read_csv(path, header=0)

df_sydney_processed = pd.get_dummies(data=my_data, columns=['Sex', 'BP', 'Cholesterol'])
X = df_sydney_processed.drop(columns='Drug', axis=1)
#X =df_sydney_processed[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
# le_sex = preprocessing.LabelEncoder()
# le_sex.fit(['F','M'])
# X[:,1] = le_sex.transform(X[:,1])


# le_BP = preprocessing.LabelEncoder()
# le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
# X[:,2] = le_BP.transform(X[:,2])



# le_Chol = preprocessing.LabelEncoder()
# le_Chol.fit([ 'NORMAL', 'HIGH'])
# X[:,3] = le_Chol.transform(X[:,3]) 


y = my_data["Drug"]

X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth =4)
drugTree.fit(X_trainset,y_trainset)
predTree = drugTree.predict(X_testset)
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))
tree.plot_tree(drugTree)
plt.show()
