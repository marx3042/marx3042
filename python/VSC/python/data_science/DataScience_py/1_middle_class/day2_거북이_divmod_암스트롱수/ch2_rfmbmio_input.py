# RFM을 이용하여 비만도를 추정하자.
sex = int(input("남성이면 0 여성이면 1을 입력하세요 "))
data = input("키-cm-와 허리 둘레-cm-를 한 칸 뛰어서 각각 입력하세요: ")

height, waist = data.split() # 공란을 경계로 분리
h, w = float(height), float(waist)

rfm = 64 - 20 * (h/w) + 12 * sex # 문자를 숫자로 분리

print("당신의 RFM : %.3f" %rfm) # .3f는 소숫점 이하는 3자리까지 의미
