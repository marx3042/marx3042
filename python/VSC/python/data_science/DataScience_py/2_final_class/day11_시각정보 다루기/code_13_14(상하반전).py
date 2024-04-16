 #
# 이미지 반전 예; 픽셀 값만 위치 이동
#
import cv2

myData_org = cv2.imread('2_final_class\day11_시각정보 다루기\myData.png', cv2.IMREAD_GRAYSCALE)
bag_org = cv2.imread('bag_cartoon.png', cv2.IMREAD_GRAYSCALE)
print(myData_org.shape, bag_org.shape)

# 이미지 반전
myData_org_rev_c = myData_org[:, ::-1] # 좌우 반전
myData_org_rev_r = myData_org[::-1, :] # 상하 반전
bag_org_rev_c = bag_org[:, ::-1] # 좌우 반전 
bag_org_rev_r = bag_org[::-1, :] # 상하 반전

cv2.imshow('myData_org', myData_org)
cv2.imshow('bag_org', bag_org)
cv2.imshow('myData_org_rev_c', myData_org_rev_c)
cv2.imshow('bag_org_rev_c', bag_org_rev_c)
cv2.imshow('myData_org_rev_r', myData_org_rev_r)
cv2.imshow('bag_org_rev_r', bag_org_rev_r)

# 이미지 크기 조절
myData_300_IN = cv2.resize(myData_org, (300, 300), interpolation=cv2.INTER_NEAREST)
myData_300_IA = cv2.resize(myData_org, (300, 300), interpolation=cv2.INTER_AREA)
bag_300_IN = cv2.resize(bag_org, (300, 300), interpolation=cv2.INTER_NEAREST)
bag_300_IA = cv2.resize(bag_org, (300, 300), interpolation=cv2.INTER_AREA)

myData_300_IA_rev_c = myData_300_IA[:, ::-1] # 이미지 반전, 모든 행에대해 열뒤집기
myData_300_IA_rev_r = myData_300_IA[::-1, :] # 이미지 반전, 모든 열에대해 행뒤집기

cv2.imshow('myData_300_IN', myData_300_IN)
cv2.imshow('myData_300_IA', myData_300_IA)
cv2.imshow('bag_300_IN', bag_300_IN)
cv2.imshow('bag_300_IA', bag_300_IA)
cv2.imshow('myData300_IA_r_col', myData_300_IA_rev_c)
cv2.imshow('myData300_IA_r_row', myData_300_IA_rev_r)

cv2.waitKey(0) # 사용자 입력을 기다림
cv2.destroyAllWindows() # 모든 창을 없애고 프로그램 종료
