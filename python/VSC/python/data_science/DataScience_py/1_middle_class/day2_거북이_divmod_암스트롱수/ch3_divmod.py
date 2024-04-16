#연산자 //와 %를 동시에 구할 수 있는 연산자 divmod

num1 = int(input('첫번째 정수를 입력하세요: '))
num2 = int(input('두번째 정수를 입력하세요: '))

q, r = divmod(num1, num2)

print(num1, "나누기", num2, "의 결과는", "몫=", q, "이고 나머지=", r, "이다")
