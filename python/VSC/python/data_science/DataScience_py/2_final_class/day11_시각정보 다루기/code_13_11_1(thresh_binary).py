#
# 관심있는 곳만 남겨 두는 작업: Threshold 사용하기
#

import cv2
global color_image, gray_image

# 트랙바가 변경되면 그 값을 임계치로 회색조 이미지를 이진화하여 창에 그림
# 임계값 x를 넘으면 최대값 255를 보여준다
def on_change_threshold(x):
   _, th_image = cv2.threshold(gray_image, x,
                               255, #최대값
                               cv2.THRESH_BINARY) # 임계값 설정 옵션: 5가지
   cv2.imshow('Thresholding', th_image)

# 윈도를 생성함
cv2.namedWindow('Thresholding')
cv2.createTrackbar('threshold', 'Thresholding', 0, 255, # 화면이름, 바 막대 이름, 최소, 최대
                  on_change_threshold) # 수행 함수명

# 촛불 이미지를 읽고, 회색조 이미지를 준비함
color_image = cv2.imread('2_final_class\day11_시각정보 다루기\candles.jpg', cv2.IMREAD_COLOR)
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY) # 영상 변환

# 처음에는 원본 이미지를 그림 (트랙바를 변경하면 임계치에 따라 이진화 결과 출력)
cv2.imshow('Thresholding', gray_image)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
