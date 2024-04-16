#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 216쪽 8.4 문
# 문제: 아래 lst에 대하여 다음을 만족하는 프로그램을 작성하시오
# 1. 중복없는 원소들로만 구성되는 리스트를 만들어 출력하시오
# 2. 중복되는 원소를 한번씩만 출력하도록 하시오
# 3. 각 숫자의 출현 빈도수를 구하여 출력하시오

lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]

# 사전을 구축하면서 빈도수를 구한다: {'키1':빈도수1, '키2': 빈도수2, .... }
lst_dic = {}
for value in lst:
    if lst_dic.get(value):
        lst_dic[value] += 1
    else:
        lst_dic[value] = 1

# 키값에 따라 순서 정렬
sorted_lst = sorted(lst_dic.items(), key=lambda x: x[0])
print(sorted_lst)
print("\n")

# 중복 없는 즉, 한번만 나타난 키들로 구성된 리스트 만들기
lst_new = []
for value in sorted_lst:
    if value[1] == 1: # 오직 한번만 나타난 것 
        lst_new.append(value[0]) # 키만 출

print('1. 중복 발생이 없는 원소 리스트 :',lst_new)


# 전체 키들로 구성된 리스트 출력
lst_new = []
for value in sorted_lst:
    lst_new.append(value[0]) # 키만 출력

print('2. 전체 원소들로 구성된 리스트 :',lst_new)

# 각 키와 발생 빈도수 출력하기
print("3. 각 원소와 발생 빈도수")
for value in sorted_lst:
    if value[1] != 1:
        print("\t", value[0], ':', value[1], '회')
no = 