student_tup = (('1111', '가길동', '010-1-1-1'), ('2222', '나길동', '010-2-2-2'), ('3333', '다길동', '010-3-3-3'))
dic_stud = {}


for i in range(len(student_tup)):
    nlist = []    
    for j in range(1,3):
        nlist.append(student_tup[i][j])    
    
    dic_stud[student_tup[i][0]] = nlist

print("학생들의 정보 목록")
print(dic_stud, sep = "\n")
    
inputnNum = input("학번을 입력하시오 : ")
for i in dic_stud.keys():
    if inputnNum == i:
        print("이름 : {}\n연락처 : {}".format(dic_stud[i][0], dic_stud[i][1]))
    
for i in dic_stud.keys():
    input_test_score = int(input())
    dic_stud[i].append(input_test_score)
print(dic_stud, sep = "\n")

sum = 0
count = 0
for i in dic_stud.keys():
    sum += dic_stud[i][-1]
    count += 1
avg = sum / count
print(round(avg, 2))


