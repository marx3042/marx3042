# 1 ~ 46까지의 범위에서  6개의 서로 다른 수로 구성되는 로또복권 번호 발생기를 작성해보자
import random

def lotto():
    nums = [ num for num in range(1, 47) ]

    num_6 =[]
    while True:
        n = random.choice(nums)
        
        if n not in num_6: # 중복 체크
            num_6.append(n)

        if len(num_6) == 6: # 6개가 생성 - 종료
            return num_6

#
for i in range(10):
    print("\t 금주의 로또 복권 번호: %s" %lotto())
