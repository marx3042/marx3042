# 비트 연산자 연습2

nums = input("두 정수를 공란으로 분리 입력하세요[예: 11 7] ")
num1, num2 = nums.split()

print("\n\n")
num1, num2 = int(num1), int(num2) # num1 = int(num1); num2 = int(num2) 과 동일. 한 줄에 2개 이상 명령문 쓸 떄
bin1, bin2 = bin(num1), bin(num2)
print("%d와 %d의 각 이진수 값은 %s와 %s이다" %(num1, num2, bin1, bin2))

num = bin(num1 & num2)
print("%d와 %d의 and-&-연산  값은 %s[%d]이다" %(num1, num2, num, int(num,2))) #int(num, 2): 이진수 num을 십진수로 변환

num = bin(num1 | num2)
print("%d와 %d의 or-|-연산  값은 %s[%d]이다" %(num1, num2, num, int(num,2)))

num = bin(num1 ^ num2)
print("%d와 %d의 xor-^-연산  값은 %s[%d]이다" %(num1, num2, num, int(num,2)))

num = bin(num1 >> num2)
print("%d를  %d만큼 right-shift >> 연산  값은 %s[%d]이다" %(num1, num2, num, int(num,2)))

num = bin(num1 << num2)
print("%d를 %d만큼  left-shit << 연산  값은 %s[%d]이다" %(num1, num2, num, int(num,2)))
