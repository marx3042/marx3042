from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1)
X_a = [[150], [145], [155], [148], [140], [160], [162], [159]]
y_a = [45, 42, 46, 44, 41, 48, 50, 46]

X_b = [[170], [167], [174], [173], [171], [165], [169], [172]]
y_b = [65, 60, 60, 58, 59, 56, 57, 66]

X_c = [[180], [183], [181], [179], [178], [183], [184], [180]]
y_c = [72, 77, 79, 78, 75, 78, 79, 77]

plt.scatter(X_a, y_a, c='red', label='a')
plt.scatter(X_b, y_b, c='blue', marker = '^', label='b')
plt.scatter(X_c, y_c, c='green', marker = 's', label='c')


plt.legend(loc='upper left')
plt.show()

#2)
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

a = zip(X_a, y_a)
l = list(a)
X1 = [list(x) for x in l]
y1 = [0] * len(X1)

b = zip(X_b, y_b)
l = list(b)
X2 = [list(x) for x in l]
y2 = [1] * len(X2)

c = zip(X_c, y_c)
l = list(c)
X3 = [list(x) for x in l]
y3 = [2] * len(X3)

human = np.array(X1 + X2 + X3)
labels = np.array(y1 + y2 + y3)

from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

X_test = [[162], [170], [182]]
y_test = [49, 57, 79]

classes = {0:'a', 1:'b', 2:'c'} 

for i in range(1 , 6):
    print('neightbors k=', 5)
    knn = KNeighborsClassifier(n_neighbors = 5) 
    knn.fit(human, labels)
    y_pred = knn.predict([[X_test[i], y_test[i]]])
    print("\t", classes[y_pred[0]])
    y_pred = knn.predict([[X_test[i], y_test[i]]])
    print("\t", classes[y_pred[0]])
    y_pred = knn.predict([[X_test[i], y_test[i]]])
    print("\t", classes[y_pred[0]])
    y_pred = knn.predict([[X_test[i], y_test[i]]])
    print("\t", classes[y_pred[0]])
    print("\n")

