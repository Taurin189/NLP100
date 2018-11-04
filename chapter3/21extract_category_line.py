# coding: utf-8
import json

wiki_json = open("jawiki-country.json", "r")
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    wiki_texts = wiki_info['text'].split("\n")
    for wiki_text in wiki_texts:
        if wiki_text.find("Category") > -1:
            print(wiki_text)
