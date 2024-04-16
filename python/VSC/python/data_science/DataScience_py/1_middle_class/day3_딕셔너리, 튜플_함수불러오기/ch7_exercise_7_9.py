#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 197쪽
#

# 함수 정의
def overlap(w1, w2):
    size = 0  # 비교할 문자의 수
    w1_pos = 0 # 첫문자열의 비교 위치
    w2_pos = len(w2) # 두번째 문자열의 비교위치
    
    if len(w1) > len(w2):
        size = len(w2)
        w1_pos = len(w1) - len(w2)
    else:
        size = len(w1)
        w2_pos = len(w1)
    
    for i in range(size):
        if w1[w1_pos + i:] == w2[:w2_pos-i]: # 겹치는 것이 있음  
            return w1[:w1_pos + i] + w2
        
    return w1 + w2 # 두 문자열 간에 겹치는게 전혀 없음 

# 실행문 
if __name__ == '__main__':
    while True:
        word1 = input('문자열1을 입력하시오(종료를 원하면 ^^ 입력) : ')
        word2 = input('문자열2을 입력하시오(종료를 원하면 ^^ 입력 : ')

        if (word1 == '^^' or word2 == '^^'):
            print("프로그램 수행 종료"); exit()
        else:
            print("\t 두 문자열 합성 결과: %s" % overlap(word1, word2))
            print("\n")
    no = 