#
# 이미지에 필터를 씌워기
#
import numpy as np
import cv2

org = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1) # 컬러 이미

kernel1 = np.ones((3, 3), np.float32) / 9
kernel1_2 = np.ones((4, 4), np.float32) / 16
kernel2 = np.ones((9, 9), np.float32) / 81

averaged33 = cv2.filter2D(org, -1, kernel1) # 입력 이미지, 이미지 깊이(-1:원래이미지), 커널
averaged44 = cv2.filter2D(org, -1, kernel1_2)
averaged99 = cv2.filter2D(org, -1, kernel2)

cv2.imshow('original', org)
cv2.imshow('filtered1', averaged33)
cv2.imshow('filtered1_2', averaged44)
cv2.imshow('filtered2', averaged99)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
