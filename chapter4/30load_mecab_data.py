# coding: utf-8
from chapter4 import dict_utils

categorized_words = dict_utils.get_dict("neko.txt.mecab")

for line in categorized_words:
    print(line)
