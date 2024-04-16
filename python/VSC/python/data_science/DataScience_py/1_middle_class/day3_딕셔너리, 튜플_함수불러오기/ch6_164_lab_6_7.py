#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-7 피보나치 함수 계산하기, 164쪽
# 피보나치 함수는 n>= 2 인 임의의 n에 대해 f(n) = f(n-1) + f(n-2)를 만족한다. 단, f(0)=f(1)=1으로 가정
#
def fib(n):
    if n == 0 or  n == 1:  # 재귀호출 중단 조건
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # 재귀호출  (n-1) + (n-2) = 2n - 3

######### 실행문
if __name__ == "__main__":   # 프로그램의 실행 부분을 정의함: main 같은 기능
    while True:
        i = int(input("몇 번째 항의 피보나치 함수 값을 원하나요? "))
        if ( i < 0):
            print("프로그램을 종료합니다")
            exit()
        else:
            print(fib(i))
            print("\n")
