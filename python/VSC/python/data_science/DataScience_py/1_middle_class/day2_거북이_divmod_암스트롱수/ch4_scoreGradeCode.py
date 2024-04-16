# 점수(score)를 실수형으로 키보드 입력받아 학점(grade)으로 변환 출력한다.
# 점수와 학점은 다음 관계를 따른다. 단, score는 0 =< score <= 100인 관계를 만족해야 한다.
# 90.0 =< score <= 100.0 이면          A
# 80.0 =< score < 90.0 이면            B
# 70.0 =< score < 80.0 이면            C
# 60.0 =< score < 70.0 이면            D
# 0.0 =< score < 60.0 이면             F

score = float(input("0~100 사이의 임의 점수를 입력하세요: "))

print("\n")

if (score > 100.0 or score < 0.0):
    print("\t점수 %f는 올바를 점수가 아닙니다. 종료합니다." % score)
    exit() # 종료

if score >= 90:
    grade ='A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score > 60:
    grade = 'D'
else:
    grade = 'F'
    
print("\t 점수 %f는 학점이 %s입니다." %(score, grade))

