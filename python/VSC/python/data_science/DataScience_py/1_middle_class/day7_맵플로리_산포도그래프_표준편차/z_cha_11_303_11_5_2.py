#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 303쪽
#
import matplotlib.pyplot as plt
import numpy as np

xData1 = [77, 78, 85, 83, 73, 77, 73, 80]
yData1 = [25, 28, 29, 30, 21, 22, 17, 35]

xData2 = [75, 77, 86, 86, 79, 83, 83, 88]
yData2 = [56, 57, 50, 53, 60, 53, 49, 61]

xData3 = [34, 38, 38, 41, 30, 37, 41, 35]
yData3 = [22, 25, 19, 30, 21, 24, 28, 18]

plt.scatter(xData1, yData1, c='red', label='Dachshund')
plt.scatter(xData2, yData2, c='blue', marker = '^', label='Samoyed')
plt.scatter(xData3, yData3, c='green', marker = 's', label='Maltese')

plt.xlabel('Length')              
plt.ylabel('Height')              
plt.title("Dog size")
plt.legend(loc='upper left')

plt.show()
