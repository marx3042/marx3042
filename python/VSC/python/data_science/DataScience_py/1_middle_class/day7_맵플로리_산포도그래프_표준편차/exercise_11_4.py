#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 303쪽 11.4
#

# 첫 데이터      ==>  x값: 평균 25 표준편차 6   y값: 평균 25 표준편차 6
# 두번째 데이터 ==>  x값: 평균 25 표준편차 6   y값: 평균 25 표준편차 3
# 세번째 데이터 ==>  x값: 평균 25 표준편차 6   y값: x 값 + 표준정규분포 난수

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(10, 3))

xData1 = 6 * np.random.randn(1000) + 25 
yData1 = 6 * np.random.randn(1000) + 25

xData2 = 6 * np.random.randn(1000) + 25
yData2 = 3 * np.random.randn(1000) + 25

xData3 = 6 * np.random.randn(1000) + 25
yData3 = []
for value in xData3:
    yData3.append(value + np.random.randn())


ax[0].scatter(xData1, yData1)
ax[1].scatter(xData2, yData2, c='red')
ax[2].scatter(xData3, yData3, c='green')

plt.show()
