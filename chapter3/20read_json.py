# coding: utf-8
import json

wiki_json = open("jawiki-country.json", "r")
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    if wiki_info["title"] == "イギリス":
        print(wiki_line)
