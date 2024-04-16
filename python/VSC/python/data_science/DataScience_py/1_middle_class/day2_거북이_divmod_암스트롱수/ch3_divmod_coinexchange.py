# 거스름 동전이 1, 10, 50, 100 및 500원일 때 주어진 거스름돈을 지불시
# 동전의 갯수를 줄여서 지불하게 하자
# won500 : 500원 동전 수, won100 :100원 동전수, won50 : 50원 동전수
# won10 : 10원 동전 수, won1 : 1원 동전수

won = int(input("거스름 돈을 나타내는 정수를 입력하세요: "))

(won500, r) = divmod (won, 500) # 500 원 동전 개수

if r == 0: # 더 거스를게 없음
    won100 = won50 = won10 = won1 = 0
else:
    (won100, r) = divmod (r, 100) # 100원 동전 개수

    if r == 0:
        won50 = won10 = won1 = 0
    else:
        (won50, r) = divmod (r, 50) # 50원 동전 개수
        
        if r == 0:
            won10 = won1 = 0
        else:
            (won10, r) = divmod (r,10) # 10원 동전 개수

            if r == 0:
                won1 = 0
            else:
                won1 = r
          

print("\n\n거스름돈 ", str(won) + "는(은)  \n" + "\t [500원짜리:" + str(won500) + "-개 " + " 100원짜리:" + str(won100) + "-개" + \
      " 50원짜리:" + str(won50) + "-개 " + " 10원짜리:" + str(won10) + "-개" + " 1원짜리:" + str(won1) + "-개] \n\t 로 거슬러 줄 수 있습니다")
