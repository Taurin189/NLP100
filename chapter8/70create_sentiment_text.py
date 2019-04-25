# coding: utf-8
import random

sentence_list = []
pos_file = open("rt-polarity.pos", "r")
for line in pos_file:
    line.replace("\n", "")
    sentence_list.append("+1 " + line)
neg_file = open("rt-polarity.neg", "r")
for line in neg_file:
    line.replace("\n", "")
    sentence_list.append("-1 " + line)

random.shuffle(sentence_list)

with open("sentiment.txt", "w") as output:
    for sentence in sentence_list:
        output.write(sentence)
