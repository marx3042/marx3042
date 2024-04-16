#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-6 평균과 중앙값 계산하기(273쪽)의 확장
# 모든 값은 전체 12자리 숫자로 소숫점 이하 2자리까지 구함

import numpy as np
# import seaborn as sbn
import matplotlib.pyplot as plt
 
players = np.zeros( (100, 3) ) # 100명의 학생들의 키, 체중(몸무게), 나이 정보 기억 리스트

# 모의 데이터 생성
players[:, 0] = 10 * np.random.randn(100) + 175 # 키
players[:, 1] = 10 * np.random.randn(100) + 70 # 체중
players[:, 2] = np.floor(10 * np.random.randn(100)) + 22 # 나이

# 키 평균과 중앙값
heights = players[:, 0] 
print('\t신장 평균값: %12.2f'% np.mean(heights)) # 12자리 수로 출력하되 소수점이하 2자리
print('\t신장 중앙값: %12.2f'% np.median(heights)); print("\n")

# 체중 평균과 중앙값
weights = players[:, 1] 
print('\t체중 평균값: %12.2f'% np.mean(weights))
print('\t체중 중앙값: %12.2f'% np.median(weights)); print("\n")

# 나이 평균과 중앙값
ages = players[:, 2] 
print('\t나이 평균값: %12.2f'% np.mean(ages))
print('\t나이 중앙값: %12.2f'% np.median(ages)); print("\n")

# 생성 정보 덤프
# print("생성된 100명의 학생 키, 몸무게 및 나이\n", players)

# 키와 체중의 상관 관계
corel = np.corrcoef(heights, weights)
print("\t키-체중 상관 관계: \n", corel)

# 산포도 그리기
plt.scatter(heights, weights)
plt.title("Heighs Vs. Weights")
plt.xlabel("Heights")
plt.ylabel("Weights")
plt.savefig("Heights-Weights_scatter.png",dpi=600)
plt.show()

# 점으로 그리기: 산포도와 같음
plt.plot(heights, weights, "sm") # square 형태로 점을 찍되 magenta 색으로
plt.title("Heighs Vs. Weights")
plt.xlabel("Heights")
plt.ylabel("Weights")
plt.savefig("Heights-Weights_plot.png",dpi=600)
plt.show()

# 막대로 그리기
plt.bar(heights, weights) 
plt.title("Heighs Vs. Weights")
plt.xlabel("Heights")
plt.ylabel("Weights")
plt.savefig("Heights-Weights_bar.png",dpi=600)
plt.show()
