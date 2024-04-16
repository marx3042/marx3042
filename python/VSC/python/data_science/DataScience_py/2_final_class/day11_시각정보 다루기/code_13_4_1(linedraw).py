# 이미지 위에 선 그리기
#
import cv2

img = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1) # 두번째 인자 '1'은 컬러 이미지를 나타냄
cv2.line(img, (0,0), (200,200), (0,0,255), 5)    # 직선의 시작점과 끝점, 색상, 두께를 지정함
cv2.arrowedLine(img, (0,200),(200,20),(0,0,255), 5) #화살표의 시작점, 끝점, 색상, 두께지정
cv2.imshow('lined', img)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드, 향후 코드에서는 생략함
cv2.waitKey(0)                       # 사용자 입력을 기다림
cv2.destroyAllWindows()              # 모든 창을 없애고 프로그램 종료
