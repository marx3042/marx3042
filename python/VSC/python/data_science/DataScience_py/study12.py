import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([1, 3, 4, np.nan, 6, 8])

countries = pd.read_csv("final_study\data\countries.csv", index_col=0)


# countries_df = pd.read_csv("final_study\data\countries.csv", index_col = 0)

# countries_df['population'].plot(kind = 'pie')

weather= pd.read_csv("final_study\data\weather.csv", index_col=0, encoding="CP949")
# weather['평균 풍속(m/s)'].plot(kind = 'hist', bins = 33)


# print(countries.head())
# print(countries[:3])
# print(countries.loc['KR'])
# print(countries['population'][:3])
# print(countries.loc['US', 'capital'])
# print(countries['population'].loc['US'])

# print(weather.describe())

# 표준편차
# print(weather.std())

weather = pd.read_csv("final_study\data\weather.csv", encoding="CP949")

monthy = [None for x in range(12)]
monthy_wind = [0 for x in range(12)]

weather['month'] = pd.DatetimeIndex(weather['일시']).month


for i in range(12):
    monthy[i] = weather[weather['month'] == (i + 1)]
    monthy_wind[i] = monthy[i].mean()['평균 풍속(m/s)']

print(weather)
plt.plot(monthy_wind, 'red')
plt.show()
