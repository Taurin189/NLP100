# coding: utf-8
import re

mecab_file = open("neko.txt.mecab", "r")
categorized_words = []

for word_line in mecab_file:
    char = word_line.split("\t")
    if len(char) >= 4:
        if re.match("動詞", char[3]) is not None:
            print(char[0])