#
# .7 선형 회귀 학습결과를 확인하고 예측하기
# 미리 "pip install scikit-learn"을 윈도우즈 cmd 모드에서 수행하여야 함

#14-6의 코드
import numpy as np 
from sklearn import linear_model  # scikit-learn 모듈을 가져온다

regr = linear_model.LinearRegression() # 학습 모델 생성

X = [[164], [179], [162], [170]]  # 다중회귀에도 사용하도록 함 
y = [53, 63, 55, 59]              # y = f(X)의 결과 
regr.fit(X, y)      # 학습 시킴

############### 회귀 함수 구하기

coef = regr.coef_            # 직선의 기울기
intercept = regr.intercept_  # 직선의 절편
score = regr.score(X, y)     # 학습된 직선이 데이터를 얼마나 잘 따르나

coef = coef[0] # 상수만 가져오기 : 대괄호 기호 없앰
if intercept < 0:
    print("\t 회귀함수 : y =", coef, "* x  - ", -intercept)
else:
    print("\t 회귀함수 : y =", coef, "* x  + ", intercept)
    
print("\t 입력 데이터들에 대한 결과 예측 적합 정도: %f" % score)

################# 새로운 데이터에 대한 예측치 알아보기
 
input_data = [ [180], [185] ]
result = regr.predict(input_data) # 결과는 리스트로 

print("\n")
print("\t 입력 데이터(키) %d에 대한 예측값(몸무게) : %f" % (input_data[0][0], result[0]))
print("\t 입력 데이터(키) %d에 대한 예측값(몸무게) : %f" % (input_data[1][0], result[1]))
# print(result)
