# coding: utf-8
from pycorenlp import StanfordCoreNLP
from chapter6.nlp_utils import get_each_sentences

sentence_list = get_each_sentences("nlp.txt")
nlp = StanfordCoreNLP('http://localhost:9000')
for sentence in sentence_list:
    res = nlp.annotate(sentence,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'xml',
                       'timeout': 1000,
                   })
    print(res)

