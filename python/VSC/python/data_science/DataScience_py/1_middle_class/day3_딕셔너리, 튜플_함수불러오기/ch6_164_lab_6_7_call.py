# 호출 및 피호출 프로그램이 "6장_함수폴더_패키지호출.pptx"와 같이 구성되어 있어야 합니다.


####### 같은 모듈에서 함수 불러오기
from ch6_164_lab_6_7 import fib # 모듈내 함수 가져오기

for i in range(30):
        print("%d-th 피보나치함수 값: %d" %(i, fib(i)) )


####### 밑에 모듈에서 함수 불러오기
# 현재 디렉토리 밑에 test란 이름의 디렉토리를 생성하고 그 안에 __init__.py란 이름의 모듈을 생성하여
# version = 1.0 이란 텍스트 한 줄을 써넣습니다(디렉토리를 모듈로 쓰기위한 파이썬의 약속!)
# 그리고 test 아래에 n!을 재귀호출로 수행하는(교과서 163쪽 내용의) 모듈(이름을 편의상 ch6_163_test_fact.py) 을 작성하고
# 팩토리얼을 계산하는 함수는 fact로 정의합니다. 그리고 이 프로그램에서 불러봅니다.

print("\n")

from test.ch6_163_test_fact import fact

for i in range(30):
        print("%d! 값: %d" %(i, fact(i)) )


