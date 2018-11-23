# coding: utf-8
import time
from chapter4 import dict_utils

time_start = time.time()
categorized_words = dict_utils.get_dict("neko.txt.mecab")
combined_words_list = []
noun_list = dict_utils.get_uniq_noun_list(categorized_words)
max_len_of_noun = dict_utils.get_max_len_of_noun(noun_list)

original_text_file = open("neko.txt", "r")
for line in original_text_file.readlines():
    for noun in noun_list:
        tmp_matched_list = []
        noun_index = line.find(noun)
        if noun_index < 0:
            continue
        tmp_text = ""
        noun_count = 0
        for s in line[noun_index + len(noun):]:
            if s is "":
                break
            tmp_text += s
            if tmp_text in noun_list:
                tmp_matched_list.append(noun + tmp_text)
            noun_count += 1
            if noun_count >= max_len_of_noun:
                break
        if len(tmp_matched_list) > 0:
            print(max(tmp_matched_list, key=len))
