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
