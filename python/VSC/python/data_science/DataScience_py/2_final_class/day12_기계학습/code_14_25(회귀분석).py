#
# 25 간단한 회귀모델과 산포도
#
import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함
import matplotlib.pyplot as plt
import numpy as np

life = pd.read_csv('2_final_class\day12_기계학습\life_expectancy.csv')
life.dropna(inplace = True)

X = life[['Alcohol', 'Percentage expenditure', 'Polio', 
          'BMI', 'GDP', 'Thinness 1-19 years']]
y = life['Life expectancy']

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.linear_model import LinearRegression
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_test_predict = lin_model.predict(X_test)

from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))
print('RMSE =', rmse) 

plt.scatter(y_test, y_test_predict)
plt.title("Life Expectancy: Real VS. Predictive")
plt.xlabel("Real Life Exp.")
plt.ylabel("Predictive Life Exp.")

z = np.linspace(35,100, 65) # y=x 기준선 
plt.plot(z, z, linewidth=2, color="red")
plt.xlim([35, 100]) # 축 표시 범위
plt.ylim([35,100])
plt.show()
