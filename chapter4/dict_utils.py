# coding: utf-8
import re

def get_dict(file_name):
    mecab_file = open(file_name, "r")
    categorized_words = []

    for word_line in mecab_file:
        char = word_line.split("\t")
        if char[0].find("EOS") < 0:
            categorized_words.append({"surface": char[0], "base": char[1], "pos": char[2], "pos1": char[3]})

    return categorized_words


def get_uniq_noun_list(dict):
    noun_list = []
    for word in dict:
        if re.match("名詞", word["pos1"]) is not None:
            noun_list.append(word["pos"])
    noun_list = list(set(noun_list))
    return noun_list


def get_max_len_of_noun(noun_list):
    return len(max(noun_list, key=len))
