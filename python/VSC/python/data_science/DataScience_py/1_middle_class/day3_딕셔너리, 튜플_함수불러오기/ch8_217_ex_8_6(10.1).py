st = [('211101', '강이안', '010-123-1111'), ('211102', '박동민', '010-123-2222'),('211103', '김수정', '010-123-3333')]

# 사전 구축 
dic = {}
for x,y,z in st: # 리스트 내 각 항목은 세개의 요소로 구성되어 있음
    dic[x] = "%s, %s" % (y,z) # 값을 두 원소로 구성되는  문자열로 간주

# 사전 출력
print("[사전 내용 출력]")
for key in dic:
    print("\t", key, dic[key])

print("\n")
# 학번 조회
while True:
    num = input("학번을 입력하세요: ")
    if (num == '-99'):
        print("\t프로그램을 종료합니다")
        exit(0)

    if num in dic:
        print("\t", dic[num]);
        print("\n")
    else:
        print("\t학번이 존재하지 않습니다")
        print("\n")



   
