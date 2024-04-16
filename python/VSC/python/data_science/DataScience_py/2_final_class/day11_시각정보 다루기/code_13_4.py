#
# 이미지 위에 선 그리기
#
import cv2

img = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1)
cv2.line(img, (0,0), (200,200), (100,200,255), 5)    # 직선의 시작점과 끝점, 색상(RGB), 두께를 지정함
cv2.arrowedLine(img, (0,200), (200,20), (50,110,55), 5) #화살표의 시작점, 끝점, 색상, 두께지정
cv2.imshow('lined', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
