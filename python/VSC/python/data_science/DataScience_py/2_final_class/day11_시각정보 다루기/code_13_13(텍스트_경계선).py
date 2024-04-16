#
# LAB 13-2 텍스트 데이터 추출을 위한 준비
#
import numpy as np
import cv2

img = cv2.imread('2_final_class\day11_시각정보 다루기\book.png')

# 잡음은 제거하면서 특징은 유지할 수 있는 양방향 필터 적용
blur_bilateral = cv2.bilateralFilter(img, 11, 75, 75)   

# 회색조로 변환
gray_img = cv2.cvtColor(blur_bilateral, cv2.COLOR_BGR2GRAY) 

# 인근 픽셀과 비교한 이진화
thresh = cv2.adaptiveThreshold(gray_img, 255,                            
         cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 7)

cv2.imshow('original', img)
cv2.imshow('bilateral', blur_bilateral)
cv2.imshow('gray', gray_img)
cv2.imshow('binary', thresh)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드로 향후 코드에서는 생략함
cv2.waitKey(0)                       # 사용자 입력을 기다림
cv2.destroyAllWindows()              # 모든 창을 없애고 프로그램 종료
