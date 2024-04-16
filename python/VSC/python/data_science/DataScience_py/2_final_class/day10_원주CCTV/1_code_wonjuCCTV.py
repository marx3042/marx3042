import pandas as pd # 정형화(2차원 테이블 구조) 파일 읽기 도구
import folium # 파이썬 지도  시각화 도구:  "pip install folium"을 윈도우즈 cmd 실행후 먼저 수행할 것
import random
import webbrowser # 지도등 웹으로 보기
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from sklearn import linear_model # scikit-learn 모듈로 회귀 분석
import numpy as np

## csv 파일 데이터 가져오기
CCTV_Wonju = pd.read_csv("E:/DataScience_py/2_final_class/day10_원주CCTV/CCTV_Wonju.csv", encoding="utf-8") # CCTV 설치 관련 csv 파일 읽어오기

print("-> 자료 앞 5개 행 내용 맛보기\n", CCTV_Wonju.head()) ; print("\n") # 앞 다섯 행 출력
print("-> 자료 맨뒤 5개 행 내용 맛보기\n", CCTV_Wonju.tail()) ; print("\n") # 뒷 다섯 행 출력
print("-> 자료의 튜플 제목(컬럼) 이름 보기\n", CCTV_Wonju.columns); print("\n") # 튜플 즉, 각 컬럼의 이름들 출력
 
## 임의의 CCTV 한 곳 위치 표시
no_of_CCTV = CCTV_Wonju['경도'].count() # CCTV 설치 총 갯수를 구한다. 경도나 위도는 NaN이 없다!
i= random.randint(0, no_of_CCTV-1) # 임의의 한 CCTV를 선택하는 인덱스
lat, lon =  CCTV_Wonju['위도'][i], CCTV_Wonju['경도'][i]
w_map = folium.Map([lat, lon], zoom_start=15) # zoom_start: 지도의 정밀도 정도로 클 수록 자세히 보여줌
folium.Marker(location=[lat, lon], popup="CCTV").add_to(w_map) # popup: 클릭시 출력될 문구

w_map.save('map1.html') # 지도 표시 웹 파일 저장
webbrowser.open('map1.html')  # 기본 부라우져 chrome으로 자동뜨게

## 전체 CCTV 위치 표시
for i in range(no_of_CCTV): 
    folium.Marker([CCTV_Wonju['위도'][i], CCTV_Wonju['경도'][i]],
                  popup=CCTV_Wonju['소재지지번주소'][i]).add_to(w_map) # 클릭시 소재지 주소가 나옴

w_map.save('map2.html')
webbrowser.open('map2.html')

##### 원주시내 동별 CCTV 설치 대수를 분석하기 위해 필요한 자료만 뽑아본다
CCTV_WJ = CCTV_Wonju[['소재지지번주소', '위도', '경도']]

# 원주시 관내 읍면동 리스트 작성
dong_name = ['문막읍', '소초면', '호저면', '지정면', '부론면', '귀래면', '흥업면', '판부면', '신림면', '중앙동',\
             '원인동', '개운동', '명륜1동', '명륜2동', '단구동', '일산동', '학성동', '단계동', '우산동', \
             '태장1동', '태장2동', '봉산동', '행구동', '무실동', '반곡관설동'] # 위키피디아 발췌, 입력

# '0'열(column)의 이름  '소재지지번주소' 를 '설치동읍면동'으로 바꿈
CCTV_WJ.rename(columns={CCTV_WJ.columns[0] : '설치읍면동'}, inplace=True) # inplace=True로 설정하여 CCTV_WJ의 해당 이름 변경 
# CCTV_WJ.to_csv("CCTV_WJ.csv", header = True, index=False, encoding = 'utf-8-sig') # csv로 저장하여 출력확인. 'utf-8-sig'로 설정

print("-> 자료 앞 5개 행 내용 맛보기\n", CCTV_WJ.head()); print("\n")
print("-> 자료의 크기(개수) \n", CCTV_WJ.count()); print("\n"); 

##### '설치읍면동' 열이 가리키는 긴 주소지를 간단한 읍면동 이름으로 바꿈
no_of_unknown =0 # 소재지 불분명한 주소도 예외적으로있을 수 있어서
for i in range(no_of_CCTV): # 전체 CCTV에 대해
    address = str(CCTV_WJ['설치읍면동'][i]) # 주소지 정보 가져오기
    flag = 0 # 주소지와 관련된 읍면동 찾았는지 여부: 0-실패, 1-성공
    for j in dong_name:
        if j in address: # 읍면동이름이 주소내에 존재하면
                CCTV_WJ.at[i, '설치읍면동'] = j   # 행 i와 열 '설치읍면동'이 만나는 곳의 값을 해당 읍면동으로 대체
                flag = 1
    if not flag: # 주소지와 관련된 읍면동 없는 경우
        CCTV_WJ.at[i, '설치읍면동'] = '기타' # '기타' 항목 추가
        no_of_unknown += 1 # 주소지 불분명 주소 갯수 누적

# print("-> 설치읍면동으로 바꾼후 내용 확인\n", CCTV_WJ); print("\n");
print("-> 자료 일반 정보 맛보기\n", CCTV_WJ.describe()); print("\n")

# 읍면동별 CCTV 설치대수 구하기
CCTV_Dong = { } #  읍면동별 설치대수를 퍼이썬 사전식로 구성
for j in dong_name: # 읍면동 이름을 '키'로
    CCTV_Dong[j] = 0 # 키: j, 값:0
    
for i in range(no_of_CCTV):
    for j in CCTV_Dong:
        if CCTV_WJ['설치읍면동'][i] == j: # 설치 읍면동이 있음
            CCTV_Dong[j] +=1 # 설치 대수 증가
            
CCTV_Dong['기타'] = no_of_unknown # 주소지 불분명 해당 갯수
print("-> 읍면동별 CCTV 설치 수\n", CCTV_Dong); print("\n")

######### 읍면동별 CCTV 설치 대수 plot
plt.figure(figsize=(10,6))
plt.bar([dong for dong in CCTV_Dong.keys()], # x-축: 읍면동 이름
        [num for num in CCTV_Dong.values()], width=0.4) # y-축: 설치 대수, width: 막대 그래프 넓이

font_path = 'Han_Go.ttf' # 한글폰트
fontprop = fm.FontProperties(fname=font_path, size=10) # 폰트 위치와 기본 크기

plt.title("원주시 읍면동 CCTV 설치 현황", fontproperties = fm.FontProperties(fname=font_path, size=15)) # 타이틀
plt.ylabel("설치대수", fontproperties = fm.FontProperties(fname=font_path, size=12)) # x-축 이름
plt.xlabel("읍면동", fontproperties = fm.FontProperties(fname=font_path, size=12)) # y-축 이름

## x-축 눈금값을 읍면동 이름으로부여함 
plt.xticks([dong for dong in CCTV_Dong.keys()],
           dong_name + ['기타'], # 맨 뒤에 소재지 불분명 '기타' 추가
           fontproperties = fontprop, rotation=30)  # x-축 값을 30도기울여 표시

# 막대 위 값 표시하기
for i, v in enumerate([dong for dong in CCTV_Dong.keys()]): # 읍면동들의 순서 색인 i와 그 이름 v
    plt.text(v, CCTV_Dong[v], str(CCTV_Dong[v]), # 막대의 맨 위에 설치 대수를 씀
             fontsize=8, color="red",
             horizontalalignment='center', verticalalignment='bottom')

# 평균 CCTV 수를 나타내는 직선을 표시하기
avg_no = sum(CCTV_Dong.values())/len(CCTV_Dong) # 평균 설치대수
plt.plot([x for x in range(len(CCTV_Dong))],
         [avg_no for x in range(len(CCTV_Dong))], # 평균치를 x-축 눈금만큼 계속 표시
         color="magenta")
plt.text(int(len(CCTV_Dong)/2), avg_no, # 중앙에 위치 시킴
         str(int(avg_no)), # 설치 대수를 적음
         color = "green",
         horizontalalignment='right', verticalalignment='bottom')

plt.savefig("wonju_cctv_install.png")
plt.show()

#### 원주시 읍면동 면적('21. 8. 18기준), 단위: km^2
Area_Dong = {'문막읍': 104.32, '소초면': 103.40, '호저면': 76.76, '지정면': 89.93, '부론면': 82.73, '귀래면': 71.52, \
             '흥업면': 59.14, '판부면': 67.98, '신림면': 127.79, '중앙동': 1.89, '원인동': 0.48, '개운동': 1.05, \
             '명륜1동': 0.92, '명륜2동': 0.95, '단구동': 3.90, '일산동': 0.80, '학성동': 0.73, '단계동': 3.69, \
             '우산동': 7.35, '태장1동': 3.04, '태장2동': 8.98, '봉산동': 7.26, '행구동': 13.55, '무실동': 9.10, \
             '반곡관설동': 21.01, '기타': 0.0}

# CCTV_Dong과 Area_Dong을 하나의 데이터 프레임 구성하기
tmp_df1 = pd.DataFrame(list(CCTV_Dong.items()),
                      columns = ['읍면동', 'CCTV 설치 수'])
tmp_df2 = pd.DataFrame(list(Area_Dong.items()),
                      columns = ['읍면동', '면적(km^2)'])

Dong = pd.merge( tmp_df1, tmp_df2, on='읍면동' ) # "읍면동", "CCTV 설치 수",  "면적(km^2)" 형태가 되게 합침
# Dong.to_csv("CCTV_AREA.csv", header = True, index=False, encoding = 'utf-8-sig') # csv로 저장하여 출력확인. 'utf-8-sig'로 설정
print("-> 읍면동별 CCTV 설치 수 및 읍면동 면적 현황 \n", Dong); print("\n")

### 면적과 CCTV 설치 수와의 상관관계 계수 계산
coeff = np.corrcoef([value for value in Area_Dong.values()],
                    [value for value in CCTV_Dong.values()])
print(coeff)
result = coeff[0][1] # 상관관계 값 가져오기
if result > 0.9 or result < -0.9:
    print("CCTV 설치 및 면적간 상관관계가 아주 높음: %s" % result)
elif result > 0.7 or result <-0.7:
    print("CCTV 설치 및 면적간 상관관계가 높음: %s" % result)
elif result > 0.4 or result < -0.4:
    print("CCTV 설치 및 면적간 상관관계가 있음: %s" % result)
elif result > 0.2 or result < -0.2:
    print("CCTV 설치 및 면적간 상관관계가  있으나 낮음: %s" % result)
else:
    print("CCTV 설치 및 면적간 상관관계가  거의 없음: %s" % result)

print("단, 음수일 경우는 반비례관계임을 나타낸다.\n")

## 면적과 CCTV 설치 수와의 상관 관계 분석을 위한 선형 회귀분석
regr = linear_model.LinearRegression() # 선형 회귀 분석 객체 생성
X = [[value] for value in Area_Dong.values()] # 2차원으로 전환 , 대문자 사용!!!
y = [value for value in CCTV_Dong.values()]
print("->읍면동 면적 벡터\n", X); print("\n")
print("-> 읍면동별 CCTV 설치 수\n", y); print("\n")

plt.figure(figsize=(10,6))
regr.fit(X,y) # 선형학습 실행
plt.scatter(X, y, color='black') # 점으로 면적 대비 CCTV 설치 수를 보임
y_pred = regr.predict(X) # 학습으로 예측치 계산: 리스트로 읍면동 수 만큼 y값 계산
plt.plot(X, y_pred, label = str(coeff), color='blue', linewidth=3)
plt.legend(loc="upper left")
plt.title("원주시 읍면동 면적(km^2)과 CCTV 설치 현황", fontproperties = fm.FontProperties(fname=font_path, size=15)) # 타이틀
plt.ylabel("CCTV 설치 대수", fontproperties = fm.FontProperties(fname=font_path, size=12)) # x-축 이름
plt.xlabel("면적(km^2)", fontproperties = fm.FontProperties(fname=font_path, size=12)) # y-축 이름
plt.savefig("CCTV_AREA_LinearReg.png")
plt.show()

                    
