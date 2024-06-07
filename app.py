
      

import nltk
# nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import Counter

# steps
# 1. read the file by line
# tokenize it by sen first and later by word
#  remove stop words 
#  check frequency a
#  most come 
#  print it 

# open file 
files = open('llm.txt', 'r')

# read files by line
text = files.read()

# chunk it to word
words = [word.lower() for word in text.split() if word.isalpha()]
# wordsb = word_tokenize(text)
# print('words manual', words)

# print('worbe', wordsb)
# remove the stopwords
stop_words = set(stopwords.words('english'))

without_stop_word_file = []

for word in words:
    if word not in stop_words:
        without_stop_word_file.append(word)

        
# check 3 the most common words
word_count = Counter(without_stop_word_file)

# using Counter from collections
print('most word', word_count.most_common(3))

# using FregDisst from nltk.probability
print('freq', FreqDist(without_stop_word_file).most_common(3))

# tfid = TfidfVectorizer()
# print(tfid)