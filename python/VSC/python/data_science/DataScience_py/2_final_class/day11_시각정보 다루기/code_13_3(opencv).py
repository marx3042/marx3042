# 실시간 컴퓨터 비젼을 위한 라이브러리 OpenCV 활용하기

import cv2

img_gray = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', cv2.IMREAD_COLOR)

print('img_gray 정보')
print(type(img_gray))
#print(img_gray.shape)
#print(img_gray.dtype); print("\n")

print('img_color 정보')
print(type(img_color))
#print(img_color.shape)
#print(img_color.dtype)

# 맨드릴 원숭이 나타내기
cv2.imshow('grayscale', img_gray)    # 화면 이름 및 회색조 이미지로 설정
cv2.imshow('color image', img_color)  # 화면 이름 및 컬러 이미지로 설정

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
