import cv2

img_gray = cv2.imread("final_study\data\ape.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("final_study\data\ape.png", cv2.IMREAD_COLOR)

cv2.imshow('grayscale', img_gray)
cv2.imshow('color image', img_color) 

cv2.waitKey(0)
cv2.destoryAllWindows()