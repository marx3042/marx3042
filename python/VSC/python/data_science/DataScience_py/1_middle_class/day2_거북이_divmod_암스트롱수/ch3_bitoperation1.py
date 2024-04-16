# 2진수, 8진수 및 16진수 사용하기: 숫자 vs. 문자열 두가지 가능
bnum = 0b11110000; bstr = '0b11110000' # 숫자 0(zero)
onum = 0o360; ostr = '0o360'            # 문자 o(oh)
hnum = 0xf0; hstr = '0xf0'

# 정수로의 변환
b1 = int(bnum); b2 = int(bstr,2)
o1 = int(onum); o2 = int(ostr, 8)
h1 = int(hnum); h2 = int(hstr, 16)
print(bnum, bstr, b1, b2)
print(onum, ostr, o1, o2)
print(hnum, hstr, h1, h2)

print("\n")

# 10진수를 2진수로
bb1 = bin(97); bb2 = bin(98) # 문자열로 기억됨
res1 = bb1+bb2
print(res1) # 0b11000010b1100010 란 문자열이 출력됨
intbb1 = int(bb1,2); intbb2 = int(bb2,2)
res2 = intbb1 + intbb2
print(res2) # 십진수값 195(=97+85)출력
print(bin(res2)) # 정상적 비트 덧셈을 수행한 결과-문자열- 0b1100001 출력
print(int(bin(res2),2)) # 위 문자열 값을 10진수로 

# bin -> oct, hex로 바꾸면 8진수나 16진수에도 적용 가능

print("\n비트연산\n")
# 비트연산 & | ^ ~ >> <<
num1 = 101; num2 = 62
print("& 연산(10진수): ", num1 & num2)
print("| 연산(10진수): ", num1 | num2)
print("^ 연산(10진수): ", num1 & num2)
print("~ 연산(10진수): ", ~num1)

print("\n")  # 다음은 데이터의 형식을 고려한 출력문의 형식의 또다른 예이다 
num3 = bin(101); num4 = bin(62); print("이진수 두 수 %s와 %s " %(num3, num4))
print("& 연산(2진수): ", bin(int(num3,2) & int(num4,2)))
print("| 연산(2진수): ", bin(int(num3,2) | int(num4,2)))
print("^ 연산(2진수): ", bin(int(num3,2) & int(num4,2)))
print("~ 연산(2진수): ", bin(~int(num3,2)))
no = 