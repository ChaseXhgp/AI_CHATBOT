# from lib2to3.pgen2 import token
import nltk
import numpy as np
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentance):
    return nltk.word_tokenize(sentance)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentance, all_words):
    """
    
    sentance = ["hello","how","are","you"]
    words = ["hi", "hello", "I", "you", "bye", "thank","cool"]
    bag = [0 , 1, 0, 1, 0, 0, 0]
    """

    sentance_words = [stem(w) for w in tokenized_sentance]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in sentance_words:
            bag[idx] = 1.0
    
    
    return bag

    

sentance = ["hello","how","are","you"]
words = ["hi", "hello", "I", "you", "bye", "thank","cool"]
bag = bag_of_words(sentance, words)

            
            