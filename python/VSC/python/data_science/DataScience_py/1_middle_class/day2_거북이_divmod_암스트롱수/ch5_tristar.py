# 차영환 교수 버전

num = int(input('숫자를 입력하세요 : '))

for i in range(num+1):
    s = ' ' * (num-i) + '*' * i
    print(s)
for i in range(num+1):
    s = '*' * i
    print(s)
