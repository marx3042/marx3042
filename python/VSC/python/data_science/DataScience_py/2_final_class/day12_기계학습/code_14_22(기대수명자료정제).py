#
# 22 기대수명 데이터 읽어오기와 결측 확인 및 자료 정제
#
import pandas as pd 

life = pd.read_csv('E:/DataScience_py/2_final_class/day12_기계학습/life_expectancy.csv')
print("===> 첫 다섯줄 내용")
print(life.head()); print("\n")

life = life[['Life expectancy', 'Year', 'Alcohol',
           'Percentage expenditure', 'Total expenditure',
           'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP',
           'Thinness 1-19 years', 'Thinness 5-9 years']]

print("===>자료 내용")
print(life); print("\n")

print("===>자료 총갯수")
print( life.shape ); print("\n")

print("===>널 자료 항목별 총갯수")
print( life.isnull().sum() ); print("\n")

life.dropna(inplace = True)
print("===>널 자료료 제외 후 자료 갯수")
print(life.shape)
