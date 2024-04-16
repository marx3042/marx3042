#
# OpenCV의 blur()를 사용한 이미지 필터링
#
import numpy as np
import cv2

org = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1)

blurred33 = cv2.blur(org, (3, 3)) # blur()함수 사용: 이미지 파일이름과 필터 사이즈
blurred99 = cv2.blur(org, (9, 9))

cv2.imshow('original', org)
cv2.imshow('blurred 3x3', blurred33)
cv2.imshow('blurred 9x9', blurred99)


# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
