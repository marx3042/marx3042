# 임의의 지름, 각, 컬러를 선택하여 원을 그리자

import random
import turtle

t=turtle.Turtle()
t.shape("turtle")

colors = ["black", "red", "yellow", "cyan", "violet", "blue", "brown", "green", "white"]

for i in range(10):
    color = random.choice(colors) # 컬러 리스트 중 한 항목 임의로 선택
    radius = random.randint(5, 100)
    angle = random.randint(5, 290)

    t.left(angle)
    t.color(color)
    t.circle(radius)

    
