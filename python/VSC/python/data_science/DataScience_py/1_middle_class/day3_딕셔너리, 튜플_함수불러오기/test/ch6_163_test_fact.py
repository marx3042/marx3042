# ch6_163_test_fact.py

# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 팩토리얼  함수 계산하기, 163쪽

def fact(n):
    if n == 0 or  n == 1:  # 재귀호출 중단 조건
        return 1
    else:
        return n* fact(n-1) 

######### 실행문
if __name__ == "__main__":   # 프로그램의 실행 부분을 정의함: main 같은 기능
    while True:
        i = int(input("원하는 팩토리얼 함수의 입력은? "))
        if ( i < 0):
            print("프로그램을 종료합니다")
            exit()
        else:
            print(fact(i))
            print("\n")
