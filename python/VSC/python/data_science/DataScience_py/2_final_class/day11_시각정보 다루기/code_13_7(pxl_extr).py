# 원하는 색깔 픽셀만 뽑아 보자
# 0~255: 256개 8-bit -> unit8
import numpy as np
import cv2

image = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # BGR -> HSV 로

# 최저 80에서 최고 130사이의 값 범위
blue_low = np.array([80, 0, 0])
blue_high = np.array([130, 255, 255])

my_mask = cv2.inRange(image_hsv, blue_low, blue_high) # 범위내 픽셀만 찾음 
print(my_mask.dtype)
cv2.imshow('original', image)
cv2.imshow('mask', my_mask)
print(image.shape)
print(my_mask.shape)

extracted_and = cv2.bitwise_and(image, image, mask= my_mask)
cv2.imshow('extracted_and', extracted_and)
extracted_or = cv2.bitwise_or(image, image, mask= my_mask)
cv2.imshow('extracted_or', extracted_or)
extracted_xor = cv2.bitwise_xor(image, image, mask= my_mask)
cv2.imshow('extracted_xor', extracted_xor)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
