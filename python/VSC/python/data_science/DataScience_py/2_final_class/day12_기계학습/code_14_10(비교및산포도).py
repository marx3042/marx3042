#
# 10 체질량지수와 당뇨수치는 어떤 상관관계가 있을까: 회귀함수 그리고 학습 및 스코어
#
from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()

X = diabetes.data[:, np.newaxis, 2]

regr.fit(X, diabetes.target)         # 학습을 통한 선형회귀 모델을 생성 

f = "y = %f * x + %f" %(regr.coef_, regr.intercept_)
print("회귀 함수:", f); print("\n")

# 학습과 시험
X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, np.newaxis, 2],
                                                    diabetes.target,
                                                    test_size = 0.2) # 20%는 시험용 나머지는 훈련용
regr = linear_model.LinearRegression() 
regr.fit(X_train, y_train)

y_pred = regr.predict(X_test)
print("\n")
print("예측치"); print(y_pred)
print("실제값"); print(y_test)
print("\n")
score = regr.score(X_train, y_train)
print("훈련 스코어: ", score)
score = regr.score(X_test, y_test)
print("시험 스코어: ", score)

plt.scatter(y_test, y_pred, color='blue', linewidth=1)
plt.title("Facts VS. Predictives")
plt.xlabel("Facts")
plt.ylabel("Predictives")
plt.show()
