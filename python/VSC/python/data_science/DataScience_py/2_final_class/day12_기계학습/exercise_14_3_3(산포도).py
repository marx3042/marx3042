#
# 품종별 체장과 높이에 관한 산포도 그리기 
#
import matplotlib.pyplot as plt
import numpy as np

# learning data
xData1 = [77, 78, 85, 83, 73, 77, 73, 80]
yData1 = [25, 28, 29, 30, 21, 22, 17, 35]

xData2 = [75, 77, 86, 86, 79, 83, 83, 88]
yData2 = [56, 57, 50, 53, 60, 53, 49, 61]

xData3 = [34, 38, 38, 41, 30, 37, 41, 35]
yData3 = [22, 25, 19, 30, 21, 24, 28, 18]

# new(test) data
x = [45, 70, 49, 60, 80]
y = [34, 59, 30, 56, 41]

plt.scatter(xData1, yData1, c='red', label='Dachshund')
plt.scatter(xData2, yData2, c='blue', marker = '^', label='Samoyed')
plt.scatter(xData3, yData3, c='green', marker = 's', label='Maltese')
plt.scatter(x, y, s=500, c='magenta', label='new Data')

plt.xlabel('Length')              
plt.ylabel('Height')              
plt.title("Physical Fearures : Dachshund, Samoyed, Maltese")
plt.legend(loc='upper left')

plt.show()
