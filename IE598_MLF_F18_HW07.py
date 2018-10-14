#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:02:54 2018

@author: hurenjie
"""
#import data
import pandas as pd
import numpy as np
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/'
                         'machine-learning-databases/wine/wine.data',
                         header=None)
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue',
                   'OD280/OD315 of diluted wines', 'Proline']
df_wine.head()

#Part 1
from sklearn.model_selection import train_test_split
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.1, 
                     stratify=y,
                     random_state=42)
    
from sklearn.ensemble import RandomForestRegressor
#from sklearn import metrics
from sklearn.model_selection import cross_val_score
import timeit
SEED = 1
rf = RandomForestRegressor(random_state= SEED)
rf.get_params()

scores=[]
a=[100,200,300,400]
for i in a:
    start = timeit.default_timer()
    rf = RandomForestRegressor(n_estimators=i, min_samples_leaf=0.12,
    random_state=SEED)
    rf.fit(X_train, y_train)
    y_train_pred = rf.predict(X_train)
    scores_rf = cross_val_score(estimator=rf,
                             X=X_train,
                             y=y_train,
                             cv=10,
                             n_jobs=1)
    stop = timeit.default_timer()
    print("n_estimator = {}".format(i))
    print(scores_rf)
    print("average score = {}".format(np.mean(scores_rf)))
    print("standard deviation = {}".format(np.std(scores_rf)))
    print('Time: ', stop - start) 
    print("\n")


#Part 2
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
feat_labels = df_wine.columns[1:]
forest = RandomForestClassifier(n_estimators=300,
                                   random_state=1)
forest.fit(X_train, y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                        feat_labels[indices[f]],
                        importances[indices[f]]))
plt.title('Feature Importance')
plt.bar(range(X_train.shape[1]),
         importances[indices],
         align='center')
plt.xticks(range(X_train.shape[1]),
               feat_labels, rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.tight_layout()
plt.show()

print("My name is RENJIE HU")
print("My NetID is: 659740767")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")

