lst = [10, 30, 40, 50, 30, 30, 20, 20, 20, 10, 30]

temp_Lst = {value for value in lst if lst.count(value) == 1}
print("중복이 없는 원소 : {}".format(temp_Lst))

temp_Lst = lst
temp_Lst = list(set(temp_Lst))
temp_Lst.sort()
print("전체 원소 : {}".format(list(temp_Lst)))

temp_Lst = {value for value in lst if lst.count(value) > 1}
temp2_Lst = list(set(temp_Lst))
temp2_Lst.sort()
for i in temp2_Lst:
    if lst.count(i) > 1:
        print("{} : {}회".format(i, lst.count(i)))