#
# 관심있는 곳만 남겨 두기: 컬러 이미지 예
#
import cv2
global color_image

# 트랙바가 변경되면 그 값을 임계치로 컬러 이미지를 이진화하여 창에 그림
def on_change_threshold(x):
   _, th_image = cv2.threshold(color_image, x, 255, cv2.THRESH_BINARY)
   cv2.imshow('Thresholding', th_image)


# 윈도를 생성함
cv2.namedWindow('Thresholding', cv2.WINDOW_NORMAL)
cv2.createTrackbar('threshold', 'Thresholding', 0, 255, on_change_threshold)

# 촛불 이미지를 읽음
color_image = cv2.imread('2_final_class\day11_시각정보 다루기\candles.jpg', cv2.IMREAD_COLOR)

# 처음에는 원본 이미지를 그림 (트랙바를 변경하면 임계치에 따라 이진화 결과 출력)
color_image = cv2.resize(color_image, (600, 400))
cv2.imshow('Thresholding', color_image)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
