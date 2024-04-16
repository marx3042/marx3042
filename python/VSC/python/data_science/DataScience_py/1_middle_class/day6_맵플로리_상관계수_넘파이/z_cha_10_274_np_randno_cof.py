import numpy as np

# 임의 50x2 난수 행렬 만들기 및 상관계수 구하기
array = np.random.rand(50,2)
first, second = array[:,0], array[:,1] # [:,0]
coef = np.corrcoef(first, second)

print("* 첫 배열: \n", first)
print("* 두번째 배열: \n", second)

print("\n")
print("* 두 배열 간의 상관 관계: \n", coef)

# 두 난수의 대응 챠트 그리기
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 9))
plt.scatter(first, second, marker = 'x')
plt.xlabel('numbers')
plt.ylabel('numbers')
plt.title("Two random numbers")
plt.savefig("TwoRandom.png", dpi=600) # 파일로 저장
plt.show()
