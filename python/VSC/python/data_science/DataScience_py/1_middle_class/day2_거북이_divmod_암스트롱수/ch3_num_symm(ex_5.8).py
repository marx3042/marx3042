# <문제>
# 입력 정수가 중앙에 위치한 수를 중심으로 대칭인지 판별한다 
# < 아이디어 >
# 대칭인 수는 앞으로 읽거나 역으로 읽어도 동일하다. 예: 12321, 343, 1234554321
# <방법>
# 수를 읽어서 10으로 자릿수 만큼 계속 나누되, 나머지를 앞자리로 이동하는 수를 구축하여
# 얻어진 수가 처음의 읽은 수와 동일한지 비교한다. 마치 주어진 수를 rotate 시키듯 !!!

while True:
    n = int(input('정수을 입력하시오 : '))
    if n == -99:
        print('프로그램을 종료합니다.')
        break # brake !
        
    t_n = n       # 입력한 수을 기억하기 위해 t_n에 복사함  
    r_n = 0       # n을 뒤집은 수를 구성하기 위한 변수이름. 처음에는 0
    i = 0 # 반복 횟수, 즉 n의 자리수만큼 되는 과정을 기억. 예, 123은 3자리 수
    print("\t [%d-th 맨끝자리 수 덜어내기] : %d \t\t\t 원래의 수 남은 것: %d " %(i, r_n, n))
    
    while n > 0:  # n의 reverse 수를 구하는 과정
        i += 1
        n, r = divmod(n, 10) # n을 10으로 나눈 후,  나머지는 r에 몫은 n에 저장
        r_n = r_n * 10 + r # 나머지를 앞으로 이동하여 뒤집은 수를 구성
        print("\t [%d-th 맨끝자리 수  덜어내기] : %d \t\t\t 원래의 수 남은 것: %d " %(i, r_n, n))
        
    if t_n == r_n:
        print('   ==> {}은(는) 대칭인 정수입니다.'.format(t_n))
    else:
        print('  ==> {}은(는) 대칭인 정수가 아닙니다.'.format(t_n))

    print("\n") # 다음 입력과 구분하기 위한 한 줄 비우기

