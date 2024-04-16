import csv
import pandas as pd
import numpy as np

#1)
column_header = ['읍면동', '중범죄', '면적']
df = pd.read_csv("Data\crimes_area.csv", header = None)
df.rename(columns = {0 : "읍면동", 1 : "중범죄 발생수", 2 : "면적"}, inplace = True)

print(df['중범죄 발생수'].mean())
print(df['면적'].mean())

#2)
df1 = df[df['중범죄 발생수'] >= 50]
print(df1)

#3)
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from sklearn import linear_model

regr = linear_model.LinearRegression()
