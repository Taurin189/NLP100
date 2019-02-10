# coding: utf-8
import nltk
from chapter6.nlp_utils import get_words

word_list = get_words("nlp.txt")
ps = nltk.stem.PorterStemmer()
for word in word_list:
    print(word + "\t" + ps.stem(word))
