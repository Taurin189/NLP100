# coding: utf-8

mecab_file = open("neko.txt.mecab", "r")
categorized_words = {}
surface = []
base = []
pos = []
pos1 = []

for word in mecab_file:
