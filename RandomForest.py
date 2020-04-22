import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def getData():

    data1 = pd.read_csv('training.txt').values

    X_train = data1[:, 0:6]
    Y_train = data1[:, 6:7]

    data2 = pd.read_csv('testing.txt').values
    X_test = data2[:, 0:6]
    Y_test = data2[:, 6:7]

    return X_train, Y_train, X_test, Y_test

X_train, Y_train, X_test, Y_test = getData()

clf = RandomForestClassifier(n_estimators=100, max_depth=4)

clf.fit(X_train, Y_train)

predicted = clf.predict(X_test)

print("********** RandomForest ************\n")


print("Accuracy: ", accuracy_score(Y_test, predicted)*100,"%")

print(confusion_matrix(Y_test, predicted))
print(classification_report(Y_test, predicted))



print("*************************\n\n")



