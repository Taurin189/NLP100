# coding: utf-8
from pycorenlp import StanfordCoreNLP
from chapter6.nlp_utils import get_each_sentences_text, get_each_sentences

sentence_list = get_each_sentences("nlp.txt")
sentence_text = get_each_sentences_text("nlp.txt")
replaced_sentence_list = []
nlp = StanfordCoreNLP('http://localhost:9000')

res = nlp.annotate(sentence_text,
                       properties={
                       'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,dcoref',
                       'outputFormat': 'json',
                       'timeout': 50000,
                   })
corefs_list = res['corefs']
for num in corefs_list:
    for text in corefs_list[num]:
        print(text)
        if not text['isRepresentativeMention']:
            print(text['text'])
