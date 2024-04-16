## 한글 워드 클라우드 예제:
# 준비: 1)한글 폰드 파일, 2)한글 stop word 파일, 3) mask 이미지

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipediaapi
from PIL import Image # 배경 이미지 사용
import numpy as np # 이미지 처리 

wiki = wikipediaapi.Wikipedia('ko')
page = wiki.page('방탄소년단')
text = page.text

# 사용할 한글 폰트가 있는 곳의 경로-파일-이름 필요
font_name = '8CWdFZ7DPDGqlF9o7-ot4M-VDac.ttf'  # https://brunch.co.kr/@jmh5531/151에서 가져옴

# 사용 안할 한글 단어 파일이 들어 있는 이름 
stop_hgl_file = 'stopwords_korean.txt' # 인터넷에서 다운 받음 ... 사이트 이름 생각 안남

f = open(stop_hgl_file, "rt", encoding="utf-8")
lines = f.readlines()
stop_words = []
for line in lines:
    line = line.replace('\n', '')
    stop_words.append(line)
f.close()

# 마스크 이미지관련 모듈
from wordcloud import ImageColorGenerator
from PIL import Image

_mask = np.array(Image.open('wine_glass.png'))
wordcloud = WordCloud(font_path=font_name, \
    #                  mask = _mask, \
                      width =3500, height = 2000, background_color='white',\
                      max_words=50, colormap='winter', stopwords=stop_words).generate(text)

plt.figure(figsize=(16, 9))
plt.imshow(wordcloud)
plt.axis("off") # 좌 우측 좌표선 나내지 않기
plt.show()
