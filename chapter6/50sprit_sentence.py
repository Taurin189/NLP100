# coding: utf-8
import re

nlp_file = open("nlp.txt", "r")

for line in nlp_file:
    line = line.replace('\n', '')
    if line:
        lines = re.sub(r'([.;:?!])\s([A-Z])', r'\1\n\2', line)
        sentences = re.split('\n', lines)
        for sentence in sentences:
            print(sentence)