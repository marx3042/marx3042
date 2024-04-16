#
# "따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)" 
# 데이터를 점으로 표현하는 산포도 그래프 그리기, 292쪽 11.4
#
import matplotlib.pyplot as plt
import numpy as np

xData = np.random.randn(10000) 
yData = np.random.randn(10000)

plt.scatter(xData, yData, alpha=0.05)
plt.title('Random Position')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
