#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 196쪽
#
word = input('문자열을 입력하세요 : ')
size = len(word)

for i in range(1, size+1): # 첫 문자부터 하나씩 늘려감
    print(word[:i])

for i in range(1, size): # 맨마지막 문자부터 없애고 하나씩 줄여감
    print(word[:-i])
