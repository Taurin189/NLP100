# coding: utf-8
import json
import re

wiki_json = open("jawiki-country.json", "r")
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    wiki_texts = wiki_info['text'].split("\n")
    for wiki_text in wiki_texts:
        category_name = re.search("(?<=====)\w+", wiki_text)
        if category_name is not None:
            print(category_name.group(0) + " 3")
            continue
        category_name = re.search("(?<====)\w+", wiki_text)
        if category_name is not None:
            print(category_name.group(0) + " 2")
            continue
        category_name = re.search("(?<===)\w+", wiki_text)
        if category_name is not None:
            print(category_name.group(0) + " 1")