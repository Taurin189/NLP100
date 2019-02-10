# coding: utf-8
from chapter6.nlp_utils import get_words

word_list = get_words("nlp.txt")
for word in word_list:
    print(word)