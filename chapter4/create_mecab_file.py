# coding: utf-8
import MeCab

m = MeCab.Tagger("-Ochasen")
original_text_file = open("neko.txt", "r")
original_text = ""
for line in original_text_file:
    original_text += line + "\n"

with open("neko.txt.mecab", "w") as output:
    output.write(m.parse(original_text))

original_text_file.close()
