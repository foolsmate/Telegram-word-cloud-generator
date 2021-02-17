#!/usr/bin/env python

import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import codecs

# Open JSON file containing the messages

data = json.load(codecs.open('result.json', 'r', 'utf-8-sig'))

arr = []

for msg in data['messages']:
    if type(msg['text']) == str:
      arr.append(msg['text'])

# Concatenate the generated array to make up a string

string = (" ").join(arr)

# Generate a word cloud, the parameters are easily tuned

wordcloud = WordCloud(width=1000,height=1000,max_font_size=30, max_words= 1000).generate(string)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()





  
