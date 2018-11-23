# coding: utf-8
import re
from chapter4 import converted_dict

categorized_words = converted_dict.get_dict("neko.txt.mecab")
noun_list = []

for line in categorized_words:
    if re.match("名詞", line["pos1"]) is not None:
        noun_list.append(line["pos"])

noun_list = list(set(noun_list))
count = 1
original_text_file = open("neko.txt", "r")
for line in original_text_file.readlines():
    print("line:" + str(count))
    count += 1
    if line.find("の") < 0:
        continue
    for first_noun in noun_list:
        first_noun = re.sub(r'(\\|\*|\+|\.|\?|\{|\}|\(|\)|\[|\]|\^|\$|\-|\||\/)', r'\\\1', first_noun)
        search_result = re.search(first_noun + "の", line)
        if search_result is not None:
            for second_noun in noun_list:
                second_noun = re.sub(r'(\\|\*|\+|\.|\?|\{|\}|\(|\)|\[|\]|\^|\$|\-|\||\/)', r'\\\1', second_noun)
                combined_search_result = re.search(first_noun + "の" + second_noun, line)
                if combined_search_result is not None:
                    print(combined_search_result.group(0))

