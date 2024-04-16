#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-8 while 문으로 별 그리기를 해보자, 131쪽
#
import turtle 
t = turtle.Turtle() 
t.shape("turtle") 
i = 0 
while i < 18:       # 가운데 그림과 같으려면 18번 반복해야 한다.
    t.forward(150)  # 150 픽셀 길이의 선분을 그린다
    t.right(140)    # 140도 거북을 회전시킨다
    i = i + 1       # 변수 i를 1만큼 증가시킨다
turtle.done()
