# input 문을 사용하여 보자
w = float(input("몸무게-kg-를 입력하세요: ")) # float는 실수 
h = float(input("키-m로 환산-를 입력하세요: "))

bmi = w / (h * h) 

print("당신의 BMI : %.3f" % bmi)
