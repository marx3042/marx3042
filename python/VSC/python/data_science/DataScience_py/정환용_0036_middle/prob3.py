import wikipedia
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wiki = wikipedia.page('computer science')

# 1)
conts = wiki.content.lower()
text = re.findall("[a-z|A-Z]+", conts)
dic_text = {word : text.count(word) for word in text}
print(dic_text)

# 2)
dic_word10 = {word : text.count(word) for word in text if text.count(word) >= 10}
wc = WordCloud(random_state = 1234,
               width = 400,
               height = 400,
               background_color = 'white')
img_wordcloud_word10 = wc.generate_from_frequencies(dic_word10)
plt.figure(figsize=(40, 30))
plt.axis('off')
plt.imshow(img_wordcloud_word10)
plt.show()

# 3)
plt.scatter(dic_word10.keys(), dic_word10.values())
plt.show()
