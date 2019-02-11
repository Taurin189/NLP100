# coding: utf-8
from pycorenlp import StanfordCoreNLP
from chapter6.nlp_utils import get_each_sentences

sentence_list = get_each_sentences("nlp.txt")
nlp = StanfordCoreNLP('http://localhost:9000')
for sentence in sentence_list:
    res = nlp.annotate(sentence,
                   properties={
                       'annotators': 'tokenize, ssplit, lemma',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
    tokens = res['sentences'][0]['tokens']
    for token in tokens:
        print(token['word'] + '\t' + token['lemma'] + '\t' + token['pos'])

