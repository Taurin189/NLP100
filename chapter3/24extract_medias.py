# coding: utf-8
import json
import re

wiki_json = open("jawiki-country.json", "r")
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    wiki_texts = wiki_info['text'].split("\n")
    for wiki_text in wiki_texts:
        ref_url = re.findall("(?<=<ref>)\w+://[\w|\/|\?|\&|\.|_|-|=|%|\'|!|#]+(?=</ref>)", wiki_text)
        if len(ref_url) > 0:
            print(ref_url)