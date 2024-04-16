# 100개의 임의의 크기 원 그리기

import turtle
import random 

t = turtle.Turtle()
t.shape('turtle')

for i in range(100): # 100개 그리기
    radius = random.randint(20, 100) # 반지름이 20~100 사이
    angle = random.randint(10,350) # 각은 10~350 사이

    t.color('blue')     # 색을 파랑으로
    t.circle(radius)
    t.left(angle)