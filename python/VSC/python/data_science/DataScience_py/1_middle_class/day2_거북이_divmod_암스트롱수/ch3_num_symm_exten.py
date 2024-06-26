# <문제>
# 입력 문자열이 중앙의 문자열을 중심으로 대칭인지 판별한다
# < 아이디어 >
# 입력을 문자열로 간주, 뒤집은 문자열과 비교한다.
#문자열 str의 역문자열은 str[::-1]로 구한다.
#

while True:
    n = input('정수나 문자열을 입력하시오(-99가 입력시 종료) : ')

    if n == '-99':
        print('프로그램을 종료합니다.')
        break # 

    n_r = n[::-1] #n의 역 문자열 구함 n[0], n[1], ..., n[-1] ---> n[ : : -1]
    if n == n_r:
        print('\t ==> {}은(는) 대칭입니다.'.format(n))
    else:
        print('\t ==> {}은(는) 대칭이 아닙니다.'.format(n))

    print("\n") # 다음 입력과 구분하기 위한 한 줄 비우기

