## working with code from Moroney (2020) 

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'Today is a sunny day',
    'Today is a rainy day'
]

## Create tokenizer object and set upper limit of 100 tokenizable words
tokenizer = Tokenizer(num_words = 100)
## fit_on_texts creates tokenized word index {'key': value_pairs}
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)

## Prints word index {'today': 1, 'is': 2, 'a': 3, 'day': 4, 'sunny': 5, 'rainy': 6}


## expanding the example
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'Today is a sunny day',
    'Today is a rainy day',
    'Is it sunny today?'
]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

## returns a list of sequences
sequences = tokenizer.texts_to_sequences(sentences)

print(sequences) ## [[1, 2, 3, 4, 5], [1, 2, 3, 6, 5], [2, 7, 4, 1]]


## OOV token out-of-vocab  
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'Today is a sunny day',
    'Today is a rainy day',
    'Is it sunny today?'
]

test_data = [
    'Today is a snowy day',
    'Will it be rainy tomorrow?'
]

## oov_token paramet (can name any string -- preferably not one being used in data)
tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

test_sequences = tokenizer.texts_to_sequences(test_data)
print(word_index) ## {'<OOV>': 1, 'today': 2, 'is': 3, 'a': 4, 'sunny': 5, 'day': 6, 'rainy': 7, 'it': 8}

## pre OOV below prints [[1, 2, 3, 5], [7, 6]] which loses context
print(test_sequences)
## currently prints [[2, 3, 4, 1, 6], [1, 8, 1, 7, 1]] which is closer to the original meaning


## padding
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    'Today is a sunny day',
    'Today is a rainy day',
    'Is it sunny today?',
    'I really enjoy walking in the snow today'
]

test_data = [
    'Today is a snowy day',
    'Will it be rainy tomorrow?'
]

tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)
## defaults to prepadding; maxlen, truncating optional
padded = pad_sequences(sequences, padding="post", maxlen=6, truncating="post")

test_sequences = tokenizer.texts_to_sequences(test_data)
print(word_index)
print(padded)
## [[ 2  3  4  5  6  0]
## [ 2  3  4  7  6  0]
## [ 3  8  5  2  0  0]
## [ 9 10 11 12 13 14]]


## removing stopwords and cleaning text
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from bs4 import BeautifulSoup
import string
## soup = BeautifulSoup(sentence)
## sentence = soup.get_text()  removes HTML tags

stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
             "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
             "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
             "he", "hed", "hes", "her", "here", "heres", "hers", "herself", "him", "himself", "his", "how",
             "hows", "i", "id", "ill", "im", "ive", "if", "in", "into", "is", "it", "its", "itself",
             "lets", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
             "our", "ours", "ourselves", "out", "over", "own", "same", "she", "shed", "shell", "shes", "should",
             "so", "some", "such", "than", "that", "thats", "the", "their", "theirs", "them", "themselves", "then",
             "there", "theres", "these", "they", "theyd", "theyll", "theyre", "theyve", "this", "those", "through",
             "to", "too", "under", "until", "up", "very", "was", "we", "wed", "well", "were", "weve", "were",
             "what", "whats", "when", "whens", "where", "wheres", "which", "while", "who", "whos", "whom", "why",
             "whys", "with", "would", "you", "youd", "youll", "youre", "youve", "your", "yours", "yourself",
             "yourselves"]

sentences = [
    'Today is a sunny day',
    'Today is a rainy day',
    'Is it sunny today?',
    'I really enjoy walking in the snow today'
]

## make transition table replaces '' with '' and removes punctation
table = str.maketrans('', '', string.punctuation)
filtered_sentences = []
for sentence in sentences:
  words = sentence.split()
  filtered_sentence = ""
  for word in words:
    if word not in stopwords:
      ## applies remove_mapping to word using translate() method
      word = word.translate(table)
      filtered_sentence = filtered_sentence + word + " "
  filtered_sentences.append(filtered_sentence)

print(filtered_sentences)
