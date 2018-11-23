# coding: utf-8
import re
from chapter4 import dict_utils

categorized_words = dict_utils.get_dict("neko.txt.mecab")

for line in categorized_words:
    if re.match("動詞", line["pos1"]) is not None:
        print(line["surface"])
