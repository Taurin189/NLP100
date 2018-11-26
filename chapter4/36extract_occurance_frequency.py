# coding: utf-8
from chapter4 import dict_utils

frequency_words_dict = dict_utils.get_frequency_word_dict("neko.txt.mecab")
frequency_words_dict = sorted(frequency_words_dict.items(), key=lambda x: -x[1])
print(frequency_words_dict)

