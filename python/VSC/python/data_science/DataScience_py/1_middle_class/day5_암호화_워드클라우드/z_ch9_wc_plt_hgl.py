## 한글 핵심어 빈도수 그리기: 챠트내 한글 깨짐이 있음

from wordcloud import WordCloud
import wikipediaapi
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

wiki = wikipediaapi.Wikipedia('ko')
page = wiki.page('방탄소년단')
text_lst = page.text.split() # 단어 리스트 생성

# matplotlib에서 한글 폰트 사용 설정
import matplotlib
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

# 사용 안할 한글 단어 파일이 들어 있는 이름 
stop_hgl_file = 'stopwords_korean.txt' # 인터넷에서 다운 받음 ... 사이트 이름 생각 안남..ㅋ 

f = open(stop_hgl_file, "rt", encoding="utf-8")
lines = f.readlines()
stop_words = []
for line in lines:
    line = line.replace('\n', '')
    stop_words.append(line)
f.close()

# 단어 수 카운트할 사전 구축
wds_dic = {}
for word in text_lst:
    if word not in wds_dic:
        wds_dic[word] = 1 # 신규 단어
    else:
        wds_dic[word] += 1 # 중복 발생

# 챠트 나타낼 단어와 빈도수 기억 리스트 구축
wds_lst = [ key for key in wds_dic if wds_dic[key] > 20 and key not in stop_words ] # 발생 단어수 50 이상
frq_lst = [ val for key, val in wds_dic.items() if wds_dic[key] > 20 and key not in stop_words ]

plt.figure(figsize=(16, 9))
plt.plot(wds_lst, frq_lst, marker = '*')
plt.xlabel('주요 키 워드')
plt.ylabel('발생 빈도수')
plt.title("위키피디아에서 '방탄소년단' 부문에서 나타난 주요 키워드와 발생 횟수")
plt.show()
