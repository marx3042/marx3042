#
# LAB 14-1 키가 비슷해도 남,녀의 몸무게는 다를 것 : 다차원 선형회귀
#
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt
 
regr = linear_model.LinearRegression() 

###### 다차원 회귀 분석
# 남자는 0, 여자는 1을 넣어 차원을 추가하였음
# 입력데이터를 2차원으로 만들어야 함

X = [[164, 1],[167, 1],[165, 0],[170, 0],[179, 0],[163, 1],[159, 0],[166, 1]]             
y = [43, 48, 47, 66, 67, 50, 52, 44]     # y 값은 1차원 데이터
regr.fit(X, y)         # 학습

print("하나의 학습 모델에 남녀를 같이 학습")
print('\t 계수 :', regr.coef_ )
print('\t 절편 :', regr.intercept_)
print('\t 점수 :', regr.score(X, y))
print('\t 은지와 동민이의 추정 몸무게 :', regr.predict([[166, 1], [166, 0]]))

######### 남여 구분하여 데이터를 준비하고 학습 한 후 그래프로 그리기
## 입력 및 출력 자료 분리 구축
x0, x1 = [], [] # 남학생, 여학생 키 리스트
y0, y1 = [], [] # 남학생, 여학생 몸무게 리스트
i = 0 # 리스트 인덱스

for val in X :
    if val[1] == 0: # 남자
        x0.append(val[0])
        y0.append(y[i])
        i +=1
    else:
        x1.append(val[0])
        y1.append(y[i])
        i += 1

X0, X1 = [ [x] for x in x0 ], [ [x] for x in x1 ] # 2차원 리스트로 확장
X0, X1 = np.array(X0), np.array(X1) # 배열로 전환
y0, y1 = np.array(y0), np.array(y1)
# print(X0, y0); print(X1, y1)

## 모델 선정과 학습
regr0 = linear_model.LinearRegression() # 새로운 학습 모델
regr1 = linear_model.LinearRegression() # 새로운 학습 모델

regr0.fit(X0, y0), regr1.fit(X1, y1) # 학습
y0_pred, y1_pred = regr0.predict(X0), regr1.predict(X1)

print("\n")
print("남녀를 서로 다른 학습 모델로  학습")
print("은지와 동민이의 추정 몸무게: ", regr1.predict([[166]]), regr0.predict([[166]]))

## 회귀분석과 출력
plt.scatter(X0, y0_pred)
plt.plot(X0, y0_pred, color="red", label ="Male")
plt.scatter(X1, y1_pred)
plt.plot(X1, y1_pred, color="blue", label ="Female")
plt.title("The Linear Regression Function: Height VS. Weight VS. Sex")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.savefig("Lab14_1.jpg", dpi=1000)
plt.legend()
plt.show()
