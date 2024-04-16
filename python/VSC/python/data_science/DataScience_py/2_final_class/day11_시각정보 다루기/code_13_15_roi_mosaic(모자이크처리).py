# 관심영역 마우스로 지정하여(selectROI) 모자이크 처리하기(resize)
# 마우스로 영역을 설정 후 임의의 키를 치면 모자이크 처리됨
# 연속해서 임의의 치를 치면 종료됨
# ROI : region of interest, 관심지역

import cv2

file_name = '2_final_class\day11_시각정보 다루기\yht_20.jpg'
rate = 30 # 모자이크 처리용 픽셀 확대비율 
title = 'mosaic' # 원도우 창 이름
img = cv2.imread(file_name) # 읽을 이미지

while True:
    x, y, w, h = cv2.selectROI(title, img, False) # 관심영역 선택
    
    if w and h: # 넓이와 높이
        roi = img[y:y+h, x:x+w]   # 관심영역 지정, 행과 열 순서로
        roi = cv2.resize(roi, (w//rate, h//rate)) # 1/rate 비율로 축소

        # 원래 크기로 확대
        roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
        img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
        cv2.imshow(title, img)  
    else:
        break

# 파일 저장
new_img = title+"_mos_."+file_name.split('.')[1]
cv2.imwrite(new_img, img)
print("%s으로 저장됨" %new_img )
        
cv2.destroyAllWindows()
