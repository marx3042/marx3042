## 문제 1: 0~99사이의 정수들 10개와 15개의 숫자들 구성되는 집합 A와 B 구하자
import random

# 초기화
A, B = set(), set()

# 집합 원소 채우기
while len(A) < 30 :
    num = random.randint(0, 99) 
    if num not in A :
        A = A | { num }

while len(B) < 20 :
    num = random.randint(0, 99) 
    if num not in B :
        B = B | { num }

print("집합 A[%d 개] : %s" %(len(A), A) )
print("집합 B[%d 개] : %s" % (len(B), B) )
print ("\n")

## 문제 2: 집합 A와 B사이의 합집합 C, 교집합 D, 및 상호 차집합 E를 구하자
C, D, E = set(), set(), set()

C = A|B #합
D = A&B #교
E = C-D #차
print("합집합 C[%d 개]: %s" %(len(C), C))
print("교집합 D[%d 개]: %s" %(len(D), D))
print("상호 차집합 E[%d 개]: %s" % (len(E), E))
print ("\n")

## 문제 3: 0~99 사이의 숫자 200 개를 생성하여 리스트 L를 구성하자.
## 그리고 L에 있는 수를 '키(key'로 중복 수를 '값(value)'로 하는 사전 DIC을 구축해여 출력하여보자
L = list()
L = [ random.randint(0,99) for num in range(200) ]

DIC = dict()

for i in L:
    if i not in DIC: # 새로운 수
        DIC[i] = 1
    else:
         DIC[i] += 1

print("리스트 L[%d 개]: %s" %(len(L), L))
print("사전 DIC[%d 개]: %s" %(len(DIC), sorted(DIC.items())))

