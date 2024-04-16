#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 303쪽
#
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

xData1 = [77, 78, 85, 83, 73, 77, 73, 80]
yData1 = [25, 28, 29, 30, 21, 22, 17, 35]

xData2 = [75, 77, 86, 86, 79, 83, 83, 88]
yData2 = [56, 57, 50, 53, 60, 53, 49, 61]

xData3 = [34, 38, 38, 41, 30, 37, 41, 35]
yData3 = [22, 25, 19, 30, 21, 24, 28, 18]

ax[0].scatter(xData1, yData1, c='red')
ax[1].scatter(xData2, yData2, c='blue', marker = 's')
ax[2].scatter(xData3, yData3, c='green', marker = '^')

ax[0].set_title("Dachshund size")
ax[1].set_title("Samoyed size")
ax[2].set_title("Maltese size")

ax[0].set_xlabel('Length')      
ax[0].set_ylabel('Height')               

ax[1].set_xlabel('Length')               
ax[1].set_ylabel('Height')           

ax[2].set_xlabel('Length')          
ax[2].set_ylabel('Height')       
plt.show()