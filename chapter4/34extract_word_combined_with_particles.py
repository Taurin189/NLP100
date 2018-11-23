# coding: utf-8
import re
import time
from chapter4 import converted_dict

time_start = time.time()
categorized_words = converted_dict.get_dict("neko.txt.mecab")
noun_list = []
combined_words_list = []
max_len_of_pos = 0

for line in categorized_words:
    if re.match("名詞", line["pos1"]) is not None:
        noun_list.append(line["pos"])
        if len(line["pos"]) > max_len_of_pos:
            max_len_of_pos = len(line["pos"])

noun_list = list(set(noun_list))
original_text_file = open("neko.txt", "r")
for line in original_text_file.readlines():
    is_in_list = False
    if line.find("の") < 0:
        continue
    for combined_word in combined_words_list:
        if line.find(combined_word) > -1:
            print(combined_word)
            is_in_list = True
    if is_in_list:
        continue
    first_noun_candidate = re.sub("([^の]+)" + "の[\S]+", r'\1', line)
    tmp_first_noun = ""
    for f in first_noun_candidate[::-1]:
        tmp_first_noun = f + tmp_first_noun
        tmp_first_noun = tmp_first_noun.replace("\n", "")
        if str(tmp_first_noun) in noun_list:
            second_noun_candidate = re.sub(tmp_first_noun + "の([\S]+)", r'\1', line)
            tmp_second_noun = ""
            count_noun = 0
            for c in second_noun_candidate:
                tmp_second_noun += c
                if tmp_second_noun in noun_list:
                    print(tmp_first_noun + "の" + tmp_second_noun)
                    combined_words_list.append(tmp_first_noun + "の" + tmp_second_noun)
                if count_noun >= max_len_of_pos:
                    break
                count_noun += 1
time_end = time.time()

print(f"経過時間：{time_end - time_start}")
