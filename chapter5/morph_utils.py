# coding: utf-8
from chapter5.Morph import Morph


def get_morph_list(file_name):
    morph_list = []
    morph_file = open(file_name, "r")
    for word_line in morph_file:
        word_line = word_line.replace("\t", ",")
        word_analysis = word_line.split(",")
        if len(word_analysis) < 9:
            continue
        tmp_morph = Morph(surface=word_analysis[0], base=word_analysis[7], pos=word_analysis[1], pos1=word_analysis[2])
        morph_list.append(tmp_morph)
    return morph_list