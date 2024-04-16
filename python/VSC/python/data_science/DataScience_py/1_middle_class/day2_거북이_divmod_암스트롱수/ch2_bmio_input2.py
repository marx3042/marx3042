# input 문을 사용하여 보자
data = input("몸무게-kg-와 키-m-를 한 칸 뛰어서 각각 입력하세요: ")

weight, height = data.split() # 공란을 경계로 분리
w, h = float(weight), float(height)

bmi = w / (h*h) # 문자를 숫자로 분리

print("당신의 BMI : %.3f" % bmi) # .3f는 소숫점 이하는 3자리까지 의미
