# 문자열 길이가 특정 수의 배수가 되게 문자 '@'를 넣는다: padding 하기 
print("\n")
v = input("임의의 문자열을 입력하세요: ")
x = int(input("임의의 양의 정수를 입력하세요: "))

z  = v # v값을 복사 해놓음
b, p = divmod(len(v),x) # len(v)를 x로 나눈 몫과 나머지

print("\n")
      
if p != 0: # 나머지가 0이 아니므로  문자열 v의 길이는 x의 배수가 아님
    print("입력 문자열 길이가 %d이므로 문자 '@'가 %d개 뒤에 추가됩니다" %(len(v), x-p)  )
    v += '@'*(x-p)

print(z); print(v)









