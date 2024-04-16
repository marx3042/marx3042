#
# 합성 사진을 제작해보기

import numpy as np
import cv2

global img1, img2     # 두 이미지를 프로그램의 전체에서 사용할 수 있도록 함

def on_change_weight(x):   # 트랙바가 움직이게 되면 이 함수가 호출된다
    weight = x / 100       # x 값이 0에서 100사이이므로 100으로 나누어 0에서 1사이 값으로
    img_merged = cv2.addWeighted(img1, 1-weight, img2, weight, 0) # 맨 끝은 추가적으로 더할 값
    cv2.imshow('Display', img_merged)

cv2.namedWindow('Display')
cv2.createTrackbar('weight', 'Display', # 조절할 값의 이름, 이미지 나올 창이름
                   0, 100, on_change_weight) # 최소값, 최댓값, 변경시 호출 함수명

img1 = cv2.imread('2_final_class\day11_시각정보 다루기\green_back.png')
img2 = cv2.imread('2_final_class\day11_시각정보 다루기\iceberg.jpg')  # iceberg.png 아님 !!!
print(img1.shape);  print(img2.shape)

img1 = cv2.resize(img1, (350,300))
img2 = cv2.resize(img2, (350,300))

cv2.imshow('Display', img1)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
