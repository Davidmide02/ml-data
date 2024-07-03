
      

import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# from nltk.stem import WordNetLemmatizer
# from nltk.stem import WordNetLemmatizer
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from google.cloud import storage
import os

start_time = time.time()
# lemmatizer = WordNetLemmatizer()
# steps
# 1. read the file by line
# tokenize it by sen first and later by word
#  remove stop words 
# lemmantize
#  check frequency a
#  most come 
#  print it 
instance_connection_name = os.getenv("INSTANCE_CONNECTION_NAME")
lemmatizer = WordNetLemmatizer()

# open file 
files = open('llm.txt', 'r')

# read files by line
text = files.read()

# chunk it to word
words = [word.lower() for word in text.split() if word.isalpha()]


# remove the stopwords
stop_words = set(stopwords.words('english'))

without_stop_word_file = [word for word in words if word not in stop_words]

     

# store the most commom word in list
most_common_word_list = []

for most_common_word, _ in FreqDist(without_stop_word_file).most_common(10):
    most_common_word_list.append(most_common_word)
    # print(most_common_word)
# print(most_common_word_list)

# vectorize the list of the most common word
tfid = TfidfVectorizer()
text_vector =tfid.fit_transform(most_common_word_list)
# print(tfid.get_feature_names_out())
# print(text_vector.todense())

# time taken for execution
end_time = time.time()
elapsed_time = end_time - start_time
print("time taken:",elapsed_time)
# time taken: 0.006171464920043945


# def get_audio_files(prefix, start, limit, num_sentences):
#     bucket_name = "development_awarri"
#     storage_client = storage.Client()
#     blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
#     most_common_word_list = {}
#     for blob in blobs:
#         most_common_word_list[blob.name] = most_common_word_list


#     if limit > count:
#         num_sentences = count
#     else:
#         pass

#     blobs = storage_client.list_blobs(bucket_name, prefix=prefix)

#     audio_files = [blob.name for blob in blobs][start:limit]
#     return audio_files, num_sentences

    # the prefix to fetch data/documents
# prefix = development_awarri/read/english/src-docs




# print("lemm:", [lemmatizer.lemmatize(word) for word in without_stop_word_file] )
# without_stop_word_file = [lemmatizer.lemmatize(word) for word in without_stop_word_file] 
# print(lemmatizer.lemmatize("running"))
# print("lemm",without_stop_word_file)
# (without_stop_word_file)
# for word in words:
#     if word not in stop_words:
#         without_stop_word_file.append(word)

# check 3 the most common words
# word_count = Counter(without_stop_word_file)

# using Counter from collections
# print('most word', word_count.most_common(3))

# using FregDisst from nltk.probability
# print('freq', FreqDist(without_stop_word_file).most_common(3))




# fetch file from the bucket

def fetch_files ():
    star_fn = time.time()
    storage_client =storage.Client()
    bucket_name = "development_awarri"
    prefix = "development_awarri/read/english/src-docs"

    # source_bucket = storage_client.bucket(bucket_name)

    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    blobs =list(blobs)
    # blobs = storage_client.list_blobs(bucket_name, prefix=prefix)
    print(blobs)
    print(type(blobs))
    for blob in blobs:
        print(blob.name)
        print(blob)
        print("here")
    end_fn = time.time()
    print("fn time:",end_fn-star_fn)
fetch_files()        