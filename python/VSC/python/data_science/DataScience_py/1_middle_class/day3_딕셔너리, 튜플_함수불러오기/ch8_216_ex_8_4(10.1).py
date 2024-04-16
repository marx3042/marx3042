lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]

# 문제 1
print ("1번 답: ", list(set(lst))); print("\n")

# 문제 2

dic = {} # 리스트내 숫자를 키로 그 발생 횟수를 값으로 하는 딕셔너리 구축

for num in lst:
    if num in dic: # 중복
        dic[num] += 1
    else: # 처음
        dic[num] = 1

d_lst =[] # 중복 숫자 리스트
for k in dic:
    if dic[k] > 1:
        d_lst.append(k)

print("2번 답: ", d_lst); print("\n")

# 문제 3
print("3번 답:")
for k in dic:
    print("%d: %d회" %(k, dic[k]))
