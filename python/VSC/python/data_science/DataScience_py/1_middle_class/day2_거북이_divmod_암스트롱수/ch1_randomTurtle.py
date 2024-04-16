# 임의로 움직이는 거북이 그리기

import turtle
from random import randint # 임의숫자 생성하는 모듈 불러오기

t = turtle.Turtle()
t.shape("turtle") # arrow, turtle, circle, square, triangle

for i in range(100): # 총 이동-좌회전-우회전-이동 동작 반복 50회
    t.forward(randint(10,100)) # 10과 100 픽셀 중 임의 선택
    t.left(randint(1,259)) # 0과 359도 중 임의 각 선택
    t.forward(randint(10,200))  # 10과 100 픽셀 중 임의 선택
    t.right(randint(0,359))  # 0과 359도 중 임의 각 선택

