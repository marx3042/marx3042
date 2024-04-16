#
#  Dachshund, Samoyed, Maltese의 몸 길이와 높이가 주어진 경우: 각기 0, 1, 2로 레이블링 후
#  K-NN 수행(k=1, 2, 3, 4, 5)
#

import numpy as np 
import matplotlib.pyplot as plt 

# 닥스 훈트의 몸 길이와 몸 높이
dachshund_length = [77, 78, 85, 83, 73, 77, 73, 80]
dachshund_height = [25, 28, 19, 30, 21, 22, 17, 35]

# 사모예드의 몸 길이와 몸 높이
samoyed_length = [75, 77, 86, 86, 79, 83, 83, 88]
samoyed_height = [56, 57, 50, 53, 60, 53, 49, 61]

# 말티즈의 몸 길이와 몸 높이
maltese_length = [34, 38, 38, 41, 30, 37, 41, 35]
maltese_height = [22, 25, 19, 30, 21, 24, 28, 18]

dachshund = zip(dachshund_length, dachshund_height)
l = list(dachshund)
X1 = [list(x) for x in l]
y1 = [0] * len(X1)   # 닥스훈트는 0으로 레이블링

samoyed = zip(samoyed_length, samoyed_height)
l = list(samoyed)
X2 = [list(x) for x in l]
y2 = [1] * len(X2)   # 사모예드는 1로 레이블링

maltese = zip(maltese_length, maltese_height)
l = list(maltese)
X3 = [list(x) for x in l]
y3 = [2] * len(X3)   # 말티즈는 2로 레이블링

dogs = np.array(X1 + X2 + X3)
labels = np.array(y1 + y2 + y3)

dogs_length = dachshund_length + samoyed_length + maltese_length
dogs_height = dachshund_height + samoyed_height + maltese_height

from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

dog_classes = {0:'Dachshund', 1:'Samoyed', 2:'Maltese'} 

for n in range(1, 6):
  print('neightbors k=', n)
  knn = KNeighborsClassifier(n_neighbors = n) 
  knn.fit(dogs, labels)
  y_pred = knn.predict([[45, 34]])
  print("\t", dog_classes[y_pred[0]])
  y_pred = knn.predict([[70, 59]])
  print("\t", dog_classes[y_pred[0]])
  y_pred = knn.predict([[49, 30]])
  print("\t", dog_classes[y_pred[0]])
  y_pred = knn.predict([[60, 56]])
  print("\t", dog_classes[y_pred[0]])
  print("\n")
