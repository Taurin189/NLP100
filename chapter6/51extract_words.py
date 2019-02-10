# coding: utf-8
import re
from chapter6.nlp_utils import get_each_sentences

sentence_list = get_each_sentences("nlp.txt")

for sentence in sentence_list:
    words = sentence.split()
    for word in words:
        word = re.sub(r'[(]?(\S+)[.,;:?!)]', r'\1', word)
        print(word)
