# coding: utf-8
from chapter5.morph_utils import get_morph_list


morph_list = get_morph_list("neko.txt.cabocha", 2)

marks_count = 0

for morph in morph_list:
    print(morph.to_list())
