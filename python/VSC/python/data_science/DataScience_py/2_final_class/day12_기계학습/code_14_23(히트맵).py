#
# 23 각 특징들 사이의 상관관계: 히트 맵
#
import matplotlib.pyplot as plt
import seaborn as sns # 히트 맵 
import pandas as pd 

life = pd.read_csv('life_expectancy.csv')

sns.set(rc={'figure.figsize':(12,10)})
correlation_matrix = life.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()
