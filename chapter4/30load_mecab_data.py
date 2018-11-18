# coding: utf-8

mecab_file = open("neko.txt.mecab", "r")
categorized_words = []

for word_line in mecab_file:
    char = word_line.split("\t")
    if len(char) >= 4:
        categorized_words.append({"surface": char[0], "base": char[1], "pos": char[2], "pos1": char[3]})

print(categorized_words)