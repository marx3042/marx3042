# 점수(score)를 실수형으로 키보드 읿력받아 학점(grade)으로 변환 출력한다.
# 점수와 학점은 다음 관계를 따른다. 단, score는 0 =< score <= 100인 관계를 만족해야 한다.
# 90.0 =< score <= 100.0 이면        A
# 80.0 =< score < 90.0 이면            B
# 70.0 =< score < 80.0 이면            C
# 60.0 =< score < 70.0 이면            D
# 0.0 =< score < 60.0 이면              F
# 만일 입력이 -88일 때까지 반복하게 while 문을 사용하여 보자 

score= 0.0  # 초기 값으로 -88아닌 임의 값을 넣어 while 문 안으로 들어가게 한다
while(score != -88):
    jumsoo = input("0~100 사이의 임의의 점수를 입력하세요(-88입력시 종료): ")
    score = float(jumsoo)

    if (score > 100.0 or score < 0.0):
        if  score != -88 :
            print("\t %.2f는 올바를 점수가 아닙니다. 다시 입력하세요" % score) #%.2f는 소숫점 이하 2자리까지를 의미
            print("\n")
            continue # 아래 부분을 수행하지 않고 다시
        else: # 수행 종료
            break  # while문을 빠져나간다

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
    
    print("\t 점수 %.2f는 학점이 %s입니다." %(score, grade));  print("\n")

print("\n"); print("프로그램을 종료합니다 !!!")
