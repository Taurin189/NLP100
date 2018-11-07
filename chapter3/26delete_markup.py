# coding: utf-8
import json
wiki_json = open("jawiki-country.json", "r")
output = []
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    wiki_texts = wiki_info['text'].split("\n")
    for wiki_text in wiki_texts:
        wiki_text = wiki_text.replace("'''''", "")
        wiki_text = wiki_text.replace("'''", "")
        wiki_text = wiki_text.replace("''", "")
        output.append(wiki_text)

for line in output:
    print(line)