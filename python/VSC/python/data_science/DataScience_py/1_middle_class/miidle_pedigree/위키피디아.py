from wordcloud import WordCloud
import wikipedia
import re
import matplotlib as plt

wiki = wikipedia.page('data science')
conts = wiki.content.lower()
text = re.findall("[a-z|A-z]+", conts)

dic_text = {word : text.count(word) for word in text if text.count(word) >= 20}

wordcloud = WordCloud(width=800, height=600).generate(conts)
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud)
plt.show()

plt.scatter(dic_text.keys(), dic_text.values())
plt.show()


