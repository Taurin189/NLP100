# coding: utf-8
import json
import re
wiki_json = open("jawiki-country.json", "r")
output = {}
tmp_dict = {}
count = 0
for wiki_line in wiki_json:
    wiki_info = json.loads(wiki_line)
    wiki_texts = wiki_info['text'].split("\n")
    template_flag = False
    for wiki_text in wiki_texts:
        if wiki_text.find("{{基礎情報") > -1:
            template_flag = True
            tmp_dict = {}
            continue
        if template_flag:
            if wiki_text.find("}}") > -1:
                template_flag = False
                output.update({count: tmp_dict})
                count += 1
                continue
            key = re.search("(?<=\|)(\s?)\S+", wiki_text)
            value = re.search("(?<==)(\s?)\s?\S+", wiki_text)
            if key is not None and value is not None:
                tmp_dict.update({key.group(0): value.group(0)})
print(output)