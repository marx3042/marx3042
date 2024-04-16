#
#  OpenCV로 이미지 필터링하기(가우시안 필터로 잡음제거)
#
import numpy as np
import cv2

org = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1)

averaged33 = cv2.GaussianBlur(org, (3,3), 1) # 1보다 크면면 표준편차가 커서 중심부가 낮아짐
averaged55 = cv2.GaussianBlur(org, (5,5), 1) 
averaged99 = cv2.GaussianBlur(org, (9,9), 1)
averaged1111 = cv2.GaussianBlur(org, (11,11), 1)

cv2.imshow('original', org)
cv2.imshow('Gaussian 33', averaged33)
cv2.imshow('Gaussian 55', averaged55)
cv2.imshow('Gaussian 99', averaged99)
cv2.imshow('Gaussian 1111', averaged1111)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
