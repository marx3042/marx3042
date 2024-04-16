#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-4 리스트에서 최댓값/최솟값을 편리하게 찾는 함수, 160쪽
#
import random

################## 함수 정의
def getMinMax(mylist, method='max'): # method 매개변수가 주어지지 않으면 max로 간주함
   minValue = 999999999999999999999999999999999 # 최솟값을 저장하기위해 아주 큰수 할당
   maxValue = -minValue # 최댓값을 저장하기위해 아주 작은수 할당

   if method == 'max' : # 최댓값 찾기
       for value in mylist:
           if value > maxValue:
               maxValue = value
       return maxValue
   elif method == 'min' : # 최솟값 찾기
       for value in mylist:
           if value < minValue:
               minValue = value
       return minValue
   else : # 미정의된 문자가 입력된 경우
       print('프로그램을 종료합니다')
       exit() # 종료

################### 실행문
# list_data = [27, 90, 30, 87, 56]
list_data = [ random.randint(0,100) for i in range(30) ] # 50~100 사이의 임의의 숫자 30개 생성
while(True):
   print("\n\n")
   list_data = [ random.randint(50,100) for i in range(30) ]
   print("[리스트 내 숫자] ", list_data)
   print("\n")
   
   s = input('   최대값을 원하면 max, 최소값을 원하면 min을 그외 입력에대해서는 종료합니다: ')
   print(getMinMax(list_data, s))
   print("\n")
