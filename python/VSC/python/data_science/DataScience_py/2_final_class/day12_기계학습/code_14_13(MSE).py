#
# 13 알고리즘이 가지는 오차(MSE)
#
from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()
regr = linear_model.LinearRegression() 

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target,
                                                    test_size = 0.2) 
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
plt.scatter(y_pred, y_test)

# 평균 제곱 오차를 구하는 함수
print('평균제곱오차(MSE): ', mean_squared_error(y_test, y_pred))

#plt.scatter(y_pred, y_test,  color='black')

x = np.linspace(0, 330, 100)  # 특정 구간의 점 : 편의상 1차 함수를 인위적으로 만듬
plt.plot(x, x, linewidth=3, color='blue')
plt.title("Facts VS. Predictive Values")
plt.xlabel("Facts")
plt.ylabel("Predictives Values")
plt.show()
