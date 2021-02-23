# importing modules
from collections import Counter
import matplotlib.pyplot as plt
import string


# reading text for analysing
with open('read.txt', 'r') as f:
  article_text = f.read()

# cleaning text
article_text = article_text.replace('\n', ' ')
cleaned_text = article_text.translate(str.maketrans('', '', string.punctuation)).lower()

# tokenizing 
tokenize_words = cleaned_text.split(' ')

# dict of stop words
stop_words = {'i', 'with', 'he', 'down', 'itself', 'm', 'shan', 'no', 'yourself', 'but', 'the', 'y', 'again', 'more', 'o', "she's", 'theirs', 'my', "isn't", 'are', 're', 'their', 'own', 'during', 'don', 'such', 'me', "you'll", 'have', 'has', 'an', 'isn', 'wouldn', 'between', 'just', 'this', 'himself', 'very', 'further', 'by', 'doing', 'so', "it's", "won't", 'out', 'not', 'ours', 'didn', 'on', 'were', 'that', 's', 'which', "don't", 'll', 'nor', "needn't", 'some', 'above', 'any', "shouldn't", "hadn't", "mightn't", 'needn', 'after', 'ourselves', 'a', "didn't", 'hers', 'until', "that'll", 'once', 'mustn', 'mightn', 'hadn', 'in', 'being', 'few', 'or', "doesn't", 't', 'been', "wasn't", 'can', 'themselves', 'up', 'to', 'it', 'for', 'had', 'haven', 'am', 'through', 'she', 'too', 'herself', 'than', 'as', 'yourselves', 'before', 'and', 'because', 'where', 'doesn', 'weren', 'under', 'whom', 'same', 'ain', 'was', 'should', 'there', 'hasn', 'shouldn', 'off', 'other', 'couldn', 'at', 'those', 'over', 'myself', "hasn't", 'your', 'be', 'do', 'why', 'does', 'below', "you've", 'd', 'aren', 'who', "should've", "mustn't", 'from', 'of', 've', "haven't", 'will', 'its', 'what', 'did', 'won', 'yours', 'you', 'him', 'if', 'each', 'both', 'while', 'how', 'they', 'about', 'we', "you'd", 'most', "couldn't", "weren't", "you're", 'here', 'wasn', 'all', 'them', 'now', "shan't", 'against', 'ma', "wouldn't", 'his', 'is', 'then', 'only', 'when', 'having', "aren't", 'into', 'these', 'our', 'her'}


# getting all emotions words into a dict
word_and_emotions = dict()
with open('emotions.txt', 'r') as f:
  for emotion in f.readlines():
    emotion = emotion.replace('\n', '').replace("'", '').replace(',', '').replace(' ', '')
    word, emot = emotion.split(':')
    word_and_emotions[word] = emot

# addign emotional_words from tokenized words to a list
emotioal_words = []
for word in tokenize_words:
  if word in word_and_emotions:
    emotioal_words.append(word)

# plotting the graph 
words_counts = Counter(emotioal_words)
# plotting
fig, ax1 = plt.subplots()
ax1.bar(words_counts.keys(), words_counts.values(), color='lightyellow', edgecolor='black')
fig.autofmt_xdate()
plt.show()

###############################################
# checking sentinal using nltk #
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def sentiment_analyse(sentiment_text):
  score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
  if score['neg'] > score['pos']:
    print(f'Negative Sentiment')
  elif score['neg'] < score['pos']:
    print(f'Positive Sentiment')
  else:
    print(f'Neutral Sentiment')

sentiment_analyse(cleaned_text)
