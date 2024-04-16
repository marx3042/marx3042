#원의 면적과 둘레 계산하기

pi = 3.141592

r = float(input("원의 반지름을 입력하세요: "))

area = pi * r * r

perimeter = r * (360/180) # 원의 각은 360도 이고 180도로 나눈다

print("원의 넓이 = %.3f  원의 둘레 = %.3f" %(area, perimeter))



