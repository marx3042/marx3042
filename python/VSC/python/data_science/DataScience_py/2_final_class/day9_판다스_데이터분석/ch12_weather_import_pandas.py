import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv("E:/DataScience_py/2_final_class/day9_data/weather.csv", encoding = "CP949")

monthy = [None for x in range(12)]
monthy_wind = [0 for x in range(12)]
weather["month"] = pd.DatetimeIndex(weather["일시"]).month

for i in range(12):
    monthy[i] = weather[weather["month"] == i + 1]  #달별로 분리
    monthy_wind[i] = monthy[i].mean()["평균풍속"]  #개별 데이터 분석

plt.plot(monthy_wind, "red")
plt.show()

