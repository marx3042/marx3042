#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 141쪽
#
start = input('시작 정수를 입력하세요 : ')
end = input('끝 정수를 입력하세요 : ')

result = 0

for i in range(int(start), int(end)+1):
    result += i
    
print(start, '에서', end, '까지 정수의 합 :', result)
