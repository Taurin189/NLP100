# coding: utf-8
from pycorenlp import StanfordCoreNLP
from chapter6.nlp_utils import get_each_sentences_text, get_each_sentences

sentence_list = get_each_sentences("nlp.txt")
sentence_text = get_each_sentences_text("nlp.txt")
replaced_sentence_list = []
nlp = StanfordCoreNLP('http://localhost:9000')
representative_dict = {}

res = nlp.annotate(sentence_text,
                       properties={
                       'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,dcoref',
                       'outputFormat': 'json',
                       'timeout': 50000,
                   })
corefs_list = res['corefs']
for num in corefs_list:
    for text in corefs_list[num]:
        representative_id = text['sentNum']
        start_num = text['startIndex']
        end_num = text['endIndex']
        if not (representative_id, start_num) in representative_dict:
            representative_dict[(representative_id, start_num)] = (end_num, text['text'])
        print(text['text'] + " " + str(text['sentNum']) + " " + str(text['startIndex']) + " " + str(text['endIndex']))
        # if not text['isRepresentativeMention']:
        #     print(text['text'])


