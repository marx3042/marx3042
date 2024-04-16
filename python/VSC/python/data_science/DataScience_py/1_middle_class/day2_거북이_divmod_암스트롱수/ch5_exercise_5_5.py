#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 142쪽
#
day = 0
height = 0

while True:
    day += 1
    height += 7
    print('day : {0:2} 달팽이의 위치 : {1:2} 미터'.format(day, height))
    if height > 29:
        print('축하합니다. 우물을 탈출하였습니다.')
        print('우물을 탈출하는 데 걸린 날은 {}일 입니다.'.format(day))
        break
    height -= 5

# a + d*i 유형 문제 즉, 7+2* (i-1) > 30 에서 i > (25)/2를 만족하는 최소 정수 i를 구한다.
# i-1을 하는 이유는 첫날 7만큼 올라가고 나머지 (i-1)날은 2씩 올라가므로
