#
# 이미지 위에 선그리기 
import cv2

img = cv2.imread('2_final_class\day11_시각정보 다루기\mandrill.png', 1)
cv2.line(img, (0,0), (200,200), (0,0,255), 5)      # 직선의 시작점과 끝점, 색상, 두께를 지정함
cv2.rectangle(img, (0,200), (200,20), (0,0,0), 5)  # 사각형의 좌표, 색상-검은색-을 지정
cv2.putText(img, "hello", (70,70), fontFace = 2, fontScale = 1, color = (0,0,0))
cv2.imshow('lined', img)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
