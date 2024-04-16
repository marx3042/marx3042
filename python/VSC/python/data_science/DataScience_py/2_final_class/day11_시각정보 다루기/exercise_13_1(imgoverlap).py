# 13.1 가방과 신발 이미지 겹치기
#
import cv2

img1 = cv2.imread('2_final_class\day11_시각정보 다루기\myData.png')
img2 = cv2.imread('2_final_class\day11_시각정보 다루기\bag_cartoon.png')

img1 = cv2.resize(img1, (300,400)); img2 = cv2.resize(img2, (300,400))

img_merged1 = cv2.addWeighted(img1, 0.5, # 첫 이미지와 가중치
                             img2, 0.5, # 두번째 이미지와 가중치
                             0) # 빛의 세기
img_merged2 = cv2.addWeighted(img1, 0.3, # 첫 이미지와 가중치
                             img2, 0.7, # 두번째 이미지와 가중치
                             0) # 빛의 세기
img_merged3 = cv2.addWeighted(img1, 0.7, # 첫 이미지와 가중치
                             img2, 0.3, # 두번째 이미지와 가중치
                             0) # 빛의 세기
img_merged1_3 = cv2.addWeighted(img1, 0.5, # 첫 이미지와 가중치
                             img2, 0.5, # 두번째 이미지와 가중치
                             3) # 빛의 세기
img_merged2_3 = cv2.addWeighted(img1, 0.3, # 첫 이미지와 가중치
                             img2, 0.7, # 두번째 이미지와 가중치
                             3) # 빛의 세기
img_merged3_3 = cv2.addWeighted(img1, 0.7, # 첫 이미지와 가중치
                             img2, 0.3, # 두번째 이미지와 가중치
                             3) # 빛의 세기

cv2.imshow('Display_0.5_0.5_0', img_merged1)
cv2.imshow('Display_0.3_0.7_0', img_merged2)
cv2.imshow('Display_0.7_0.3_0', img_merged3)
cv2.imshow('Display_0.5_0.5_3', img_merged1_3)
cv2.imshow('Display_0.3_0.7_3', img_merged2_3)
cv2.imshow('Display_0.7_0.3_3', img_merged3_3)

cv2.waitKey(0) # 사용자 입력을 기다림
cv2.destroyAllWindows() # 모든 창을 없애고 프로그램 종료
