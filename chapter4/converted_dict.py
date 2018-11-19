# coding: utf-8


def get_dict(file_name):
    mecab_file = open(file_name, "r")
    categorized_words = []

    for word_line in mecab_file:
        char = word_line.split("\t")
        if char[0].find("EOS") < 0:
            categorized_words.append({"surface": char[0], "base": char[1], "pos": char[2], "pos1": char[3]})

    return categorized_words