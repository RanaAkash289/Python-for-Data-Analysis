# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 03:15:12 2024

@author: Akash Rana
"""
# pip install wordcloud
# pip install langdetect
# pip install sumy
# pip install textblob

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from langdetect import detect
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from textblob import TextBlob
import seaborn as sns

#Reading the csv file
df = pd.read_csv('chatgpt1.csv')

#Creating a function to detect the languages
x = df['Text'][0]
lang = detect(x)

def det(x):
    try:
        lang = detect(x)
    except:
        lang = 'Other'
    return lang

df['lang'] = df['Text'].apply(det)
df = df.loc[df['lang'] == 'en']
df = df.reset_index(drop=True)

#Cleaning some text
#df['Text'] = df['Text'].str.replace('amp','')
#df['Text'] = df['Text'].str.replace('http','')
#df['Text'] = df['Text'].str.replace('t.co','')

#Developing Sentiment funtion
def get_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['Text'].apply(get_sentiment)

#Generate a word cloud
comments_word = ''
stop_words = set(STOPWORDS)

for val in df.Text:
    val = str(val)
    tokens = val.split()
    comments_word = comments_word + " ".join(tokens) + " " 

wordcloud = WordCloud(width=900, height=500, background_color='black', 
                      stopwords = stop_words, min_font_size=10).generate(comments_word)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout()
plt.show()

sns.set_style('whitegrid')
plt.figure(figsize=(10,5))

sns.countplot(x = 'sentiment', data = df)
plt.xlabel('Sentiment')
plt.ylabel('Count of Sentiment')
plt.title('Sentiment Distribution')
plt.show()

























































