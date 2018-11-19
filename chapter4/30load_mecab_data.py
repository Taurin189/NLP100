# coding: utf-8
from chapter4 import converted_dict

categorized_words = converted_dict.get_dict("neko.txt.mecab")

for line in categorized_words:
    print(line)
