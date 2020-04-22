# Plot ad hoc mnist instances
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
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


clf = MLPClassifier(solver='lbfgs', activation = 'logistic', alpha=1e-5,
                    hidden_layer_sizes=(16, 16), random_state=1, warm_start=True)

clf.fit(X_train, Y_train)                         

predicted = clf.predict(X_test)

print("********** NN ************\n")


print("Accuracy: ", accuracy_score(Y_test, predicted))

print(confusion_matrix(Y_test, predicted))
print(classification_report(Y_test, predicted))

print("*************************\n\n")




