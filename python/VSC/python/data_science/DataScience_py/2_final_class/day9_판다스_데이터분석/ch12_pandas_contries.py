import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 인덱스[0] 을 인덱스로 사용할지 일반 인덱스로 사용할지
df = pd.read_csv("E:/DataScience_py/2_final_class/day9_data/countries.csv", index_col=0)
index_no_df = pd.read_csv("E:/DataScience_py/2_final_class/day9_data/countries.csv")

# 인덱스 열의 이름과 열 같은지 확인
print(index_no_df["population"])
print(df['population'])

# barplot 다른 방법 : seaborn 사용하지 않고 하는 방법
df['population'].plot(kind = "bar", color = ('b', 'darkorange', 'g', 'r', 'm'))
plt.show()
#원 그래프
df['population'].plot(kind = "pie")
plt.show()



