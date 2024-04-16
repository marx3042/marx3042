# 주어진 초단위에 대해 년월일시간 계산하기 
# y: year, d: day, h: hour, m: minute, s; sec

sec = int(input("초를 나타내는 정수를 입력하세요: "))

(y, x) = divmod (sec, 86400 * 365) # 1년은 86400 * 365 초

if x == 0:
    d = h = m = 0
else:
    (d, x) = divmod (x, 86400) # 1일은 86400(= 24 x 60 x 60) 초

    if x == 0:
       h = m = 0
    else:
        (h, x) = divmod (x, 3600) # 1 시간은 3600(= 60 x 60) 초
        
        if x == 0:
            m = 0
        else:
            (m, x) = divmod (x, 60)

print(str(sec) + "초는  " + str(y) + "-년  " + str(d) + "-일  " + str(h) + \
          "-시간  " + str(m) + "-분  " + str(x)+ "-초입니다") # \는 이음 줄 표시 기호
