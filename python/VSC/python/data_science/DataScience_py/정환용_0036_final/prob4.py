# iris의 꽃잎과 꽃말 데이터를 가지고 기계학습 시켜 정확도 분석
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.2)

num_neigh = 1
knn = KNeighborsClassifier(n_neighbors = num_neigh)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test, y_pred)
print("n_neighborsrk {0:d}일때 정확도 : {1:.3f}".format(num_neigh, scores))