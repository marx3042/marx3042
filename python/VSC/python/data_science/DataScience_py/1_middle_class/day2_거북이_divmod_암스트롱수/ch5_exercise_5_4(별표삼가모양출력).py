#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 142쪽
#
number = int(input('숫자를 입력하세요 : '))

for height in range(number):
    
    for space in range(number - height - 1):
        print(' ', end='')
        
    for star in range(height + 1):
        print('*', end='')
        
    print('')
