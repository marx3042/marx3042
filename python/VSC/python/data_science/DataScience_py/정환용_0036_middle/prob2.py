import random
import numpy as np

numberLst = []
numLst1 = []
numLst2 = []

for i in range(30, 101):
    numberLst.append(i)

# 1)
for i in range(60):
    numLst1.append(random.choice(numberLst))    
    numLst2.append(random.choice(numberLst))

# 2)
set_lst_01 = set(numLst1)
set_lst_02 = set(numLst2)
print("AA의 집합은 {}".format(set_lst_01))
print("BB의 집합은 {}".format(set_lst_02))

# 3)
plus_Lst = []
equal_Lst = []
minus_Lst = []

numLst01 = list(set_lst_01)
numLst02 = list(set_lst_02)

for i in range(len(numLst01)):
    for j in range(len(numLst02)):
        if numLst01[i] == numLst02[j]:
            equal_Lst.append(numLst01[i])
            
plus_Lst = numLst01 + numLst02
plus_Lst = set(plus_Lst)

minus_lst = numLst01 + numLst02
for i in range(len(equal_Lst)):
    for j in range(len(minus_Lst)):
        if equal_Lst[i] == minus_Lst[j]:
            minus_Lst.remove(equal_Lst[i])

print("합집합")
print(plus_Lst)
print("교집합")
print(equal_Lst)
print("대칭차집합")
print(minus_Lst)





