#
# 흐림 필터로 잡음을 제거
#
import numpy as np
import cv2

original_image = cv2.imread('2_final_class\day11_시각정보 다루기\salt_pepper.png', 0) # 소금과 후추 잡음 이미지
result_image3 = cv2.medianBlur(original_image,  3) # 3x3 필터
result_image5 = cv2.medianBlur(original_image,  5) # 5x5 필터
result_image9 = cv2.medianBlur(original_image,  9) # 9x9 필터

cv2.imshow('original', original_image)
cv2.imshow('medianBlur_3', result_image3)
cv2.imshow('medianBlur_5', result_image5)
cv2.imshow('medianBlur_9', result_image9)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
