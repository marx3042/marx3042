## 파일내의 단어 바꾸기 및 RE 적용 연습

################### 빈도수 조사
from wordcloud import WordCloud, STOPWORDS
import wikipedia
import re

wiki = wikipedia.page("Deep Learning")
conts = wiki.content.lower()
text_lst = list(conts.split()) # 단어들의 리스트 구성

print("원래 문서 내용")
print(conts)

# 영어 단어의 경우 첫 문자를 대문자로 하여  바꾸어보자
new_word = []
for word in text_lst:
    if word[0].isalpha():
        new_word.append(word[0].upper())
    else:
        new_word.append(word)

new_conts =' '.join(new_word)

print("각 영어 단어를 첫 글자의 대문자로 바꾼 결과")
print("new_contents", new_conts)

# 금지어 리스트 내에 속하는 단어들을 제거해보자
# 다음과 같은 기호로 시작되는 단어: (, ", =, | , %, _, -, ., {, \, /, < 등등외 숫자

# 방법1: 제거 대상 기호로 시작하는 단어 제거
words1 = ""
words1= re.sub('[\d|(|"|=|\||%|_|-|.|/|\\|+|<|>|)|,]', '', conts)
print("특수 문나자나 기호를 제거한 후 결과") 
print(words1) # 특수 기호가 너무 많아 그래도 남아 있네요.

# 방법2: 알파벧 대소문자로만 구성되는 단어들만 남기기
words2 = []
words2 = re.findall('[a-z|A-Z]+', conts) # 문서내 영어 단어만 추출
print(' '.join(words2))
        
