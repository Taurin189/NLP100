# coding: utf-8
from chapter5.morph_utils import get_morph_list


morph_list = get_morph_list("neko.txt.cabocha")

marks_count = 0

for morph in morph_list:
    if marks_count == 2:
        print(morph.to_list())
    if marks_count > 2:
        break
    if morph.base == "。":
        marks_count += 1
