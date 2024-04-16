from sqlalchemy import true

arList = []

for i in range(3):
    inputfruit = input("좋아하는 과일 이름을 입력하시오: ")
    arList.append(inputfruit)

bestfruit = input("과일의 이름을 입력하시오: ")
if bestfruit in arList:
    print("이 과일은 당신이 좋아하는 과일입니다.")
else :
    print("이 과일은 당신이 좋아하는 과일이 아닙니다.")    

    
