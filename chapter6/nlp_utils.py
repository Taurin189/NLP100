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


def get_each_sentences_text(filename):
    nlp_file = open(filename, "r")
    sentence_text = ""
    for line in nlp_file:
        line = line.replace('\n', '')
        if line:
            lines = re.sub(r'([.;:?!])\s([A-Z])', r'\1\n\2', line)
            sentences = re.split('\n', lines)
            for sentence in sentences:
                sentence_text += sentence + "\n"
    return sentence_text

def get_words(filename):
    sentence_list = get_each_sentences(filename)
    word_list = []
    for sentence in sentence_list:
        words = sentence.split()
        for word in words:
            word = re.sub(r'[(]?(\S+)[.,;:?!)]', r'\1', word)
            word_list.append(word)
    return word_list