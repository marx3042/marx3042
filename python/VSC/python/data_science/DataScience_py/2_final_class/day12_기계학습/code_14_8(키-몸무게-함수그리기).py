#
# 8. 선형회귀로 예측하기 : 키와 몸무게간의 회귀함수 그리기
#
import matplotlib.pyplot as plt
import numpy as np 
from sklearn import linear_model  # scikit-learn 모듈을 가져온다

regr = linear_model.LinearRegression() # 학습 모델 선정 
X = [[164], [179], [162], [170]]  # 선형회귀의 입력은 2차원으로 만들어야 함
y = [53, 63, 55, 59]            # y = f(X)의 결과값
regr.fit(X, y)      # 학습

print(X,y)

# 학습 데이터와 y 값을 산포도로 시각화 
plt.scatter(X, y, color='black')

# 학습 데이터를 입력으로 하여 예측값을 계산
y_pred = regr.predict(X)

### 상관 계수 구하기
X = np.array(X) # 일단 입력 데이터 2차원 리스트를 배열로 변환
x = X.flatten() # 1차원 벡터 즉, 스칼라형의 다시 변환 

corcof = np.corrcoef([x,y]) # 상관 관계 구하기
print("키와 몸무게 간의 상관 계수\n"); 
print(corcof)

# 학습 데이터와 예측값으로 선그래프로 나나탬
# 계산된 기울기와 y 절편을 가지는 직선을 보여줌
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.title("The Linear Regression Function: Heights VS. Weights")
plt.ylabel("Weights")
plt.xlabel("Heights")
plt.savefig("14_8.png", dpi=600)
plt.show()



