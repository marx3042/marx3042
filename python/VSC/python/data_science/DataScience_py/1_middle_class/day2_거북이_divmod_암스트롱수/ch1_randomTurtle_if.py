# 임의로 움직이는 거북이 그리기
# 좌우 이동을 확률적으로 선택하기

import turtle
from random import randint # 임의숫자 생성하는 모듈 불러오기

t = turtle.Turtle()
t.shape("turtle")

for i in range(100): # 총 이동-좌회전-우회전-이동 동작 반복
    num = randint(0,9) 

    if num >= 5: # 1/2 확률로 좌회전 
        t.forward(randint(5,150)) # 5와 150 픽셀 중 임의 선택
        t.left(randint(0,359)) # 0과 359도 중 임의 각 선택
    else: # 1/2 확률로 우회전
        t.forward(randint(5,150))  # 5와 150 픽셀 중 임의 선택
        t.right(randint(0,359))  # 0과 359도 중 임의 각 선택

