#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 217쪽 문제 8.6
# 문제 1. 아래 student_tuple로 부터 '학번:(이름, 전번)'의 딕셔너리를 만들어 출력하는 프로그램을 작성하시오.
# 문제 2. 구축된 딕셔너리를 이용해서 학번을 입력하면 이름과 전번을 출력하는 프로그램을 작성하시오.
student_tuple = [('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'),('211103', '김수정', '010-123-3333')]

student_dic = {} # 구축할 사전 이름
for student in student_tuple:
    number, name, phone = student  # 리스트 내 각 튜플이 3개의 요소로 구성되어 있음
    student_dic[number] = [name, phone] # 이름과 전번을 리스트로 하여 학번 '키'에 대응하는 값으로 사전 구성

print("\n")
print("학번을 키로 이름과 전번을 리스트로 하여 키에 대응하는 값으로 기억하는 사전(딕셔너리)")
print("student 사전", student_dic); print("\n")

for key, value in student_dic.items(): # 사전의 각 item에 대해 출력
    print(key + " :",value)

print("\n")

while True:
    number = input("학번을 입력하시오(-99입력시 종료) : ")
    if (number == '-99') :
        print("프로그램을 종료합니다.")
        exit()

        
    flag = False # 학번이 사전에 존재하는지 나타냄

    for key, value in student_dic.items():
        if key == number:
            print(number + ' 학생은 ' + student_dic[number][0] + '이며, 전화번호는 ' + student_dic[number][1] + '입니다.')
            flag =True # 일치하는 학번 존재
            break
        else:
            continue

    if (not flag): # 사전에 존재하는 키 즉, 학번이가 아님
        print(number, "는 올바른 학번이 아닙니다")
