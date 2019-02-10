# coding: utf-8
import re


def get_each_sentences(filename):
    nlp_file = open(filename, "r")
    sentence_list = []
    for line in nlp_file:
        line = line.replace('\n', '')
        if line:
            lines = re.sub(r'([.;:?!])\s([A-Z])', r'\1\n\2', line)
            sentences = re.split('\n', lines)
            for sentence in sentences:
                sentence_list.append(sentence)
    return sentence_list