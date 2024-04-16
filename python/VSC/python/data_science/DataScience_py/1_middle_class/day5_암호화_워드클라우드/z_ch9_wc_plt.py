# 영어 단어 클라우드, 단어 카운트 및 차트로 그리기

from wordcloud import WordCloud, STOPWORDS
import wikipedia
import matplotlib.pyplot as plt

wiki = wikipedia.page('Deep Learning')
page = wiki.content # 텍스트만 발췌
page = page.lower()
text_lst = page.split() # 단어 리스트 생성

# 단어 수 카운트할 사전 구축
wds_dic = {}
for word in text_lst:
    if word not in wds_dic:
        wds_dic[word] = 1 # 신규 단어
    else:
        wds_dic[word] += 1 # 중복 발생

# 조사나 관사 등 키워드에서 뺄 단어들(금지어) 리스트 구성
stop_words = list( STOPWORDS | { 'one', 'two', 'using', 'make', 'use', 'The', '==', '===', 'used' } ) # 결과를 보면서 가감

# 워드 클라우드
wordcloud = WordCloud(width = 2000, height = 1500,
                      stopwords = stop_words).generate(page)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show()
    
# 챠트 나타낼 단어와 빈도수 기억 리스트 구축
wds_lst = [ key for key in wds_dic if wds_dic[key] > 20 and key not in stop_words ] # 발생 단어수 50 이상
frq_lst = [ val for key, val in wds_dic.items() if wds_dic[key] > 20 and key not in stop_words ]

plt.figure(figsize=(16, 9))
plt.scatter(wds_lst, frq_lst, marker = '*')
plt.xlabel('Major Keywords')
plt.ylabel('Frequency')
plt.title("Major Keywords and Their Frequency")
plt.savefig("Keywords_Freq.png", dpi=600) # 파일로 저장
plt.show()
