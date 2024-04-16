#
# 다양한 흐림 필터로 잡음을 제거
#
import numpy as np
import cv2

original_image = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1)
result_image1 = cv2.GaussianBlur(original_image,  (9,9), 1)
result_image2 = cv2.medianBlur(original_image, 9)
result_image3 = cv2.bilateralFilter(original_image, # 양방향필터: 공간과 색상 필터 
                                    9, # 커널영역 지름
                                    50, # 색생 필터
                                    50) # 가우스 필터(공간 필터)
result_image4 = cv2.bilateralFilter(original_image, # 양방향필터: 공간과 색상 필터 
                                    5, # 커널영역 지름
                                    50, # 색생 필터
                                    50) # 가우스 필터(공간 필터)

cv2.imshow('original', original_image)
cv2.imshow('Gauss', result_image1)
cv2.imshow('medianBlur', result_image2)
cv2.imshow('bilateralFilter_9', result_image3)
cv2.imshow('bilateralFilter_5', result_image4)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
