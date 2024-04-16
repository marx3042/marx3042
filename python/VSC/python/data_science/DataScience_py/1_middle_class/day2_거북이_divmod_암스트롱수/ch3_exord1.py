# python에서의 문자열 구성과 관련된 몇가지 예 
n = input("무엇이든 입력해보세요: "); print(n)

s = "입력 문자열: %s 입니다" % n
print(s)

t = s * 3 # 3회 입력문자열 출력
print(t)

for i in range(10):
    u = "** %s ** %s ++" % ("@@@", i) # 입력문자열과 i값을 붙여서 출력
    print(u)










