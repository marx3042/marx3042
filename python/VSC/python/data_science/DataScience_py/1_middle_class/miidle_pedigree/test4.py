shop = {"사과" : 0, '배' : 0, "수박" : 0, "귤" : 0, '포도' : 0}
count = 0
inputNum = list(map(int, input("사과, 배 수박, 귤, 포도 가격을 공백으로 구분하여 입력 : ").split()))
for i in shop.keys():
    shop[i] = inputNum[count]
    count+=1

print("-------오늘의 과일 가격---------")
for i in shop.keys():
    print("{}  :  {}원 ".format(i, shop[i]))

inputName = input("구매를 원하는 과일의 이름을 입력하시오 : ")

for i in shop.keys():
    if i == inputName:
        print("오늘의 {}가격은 {} 원 입니다.".format(i, shop[i]))

