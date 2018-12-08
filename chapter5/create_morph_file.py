# coding: utf-8
import CaboCha

original_text_file = open("neko.txt", "r")
original_text = ""

p = CaboCha.Parser()

for line in original_text_file:
    original_text += line + "\n"

tree = p.parse(original_text)
morph_list = tree.toString(CaboCha.FORMAT_LATTICE).split("\n")
with open("neko.txt.cabocha", "w") as output:
    for morph in morph_list:
        output.write(morph + "\n")

original_text_file.close()