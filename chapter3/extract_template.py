# coding: utf-8
import json
import re


def get_country_information(json_obj):
    output = {}
    tmp_dict = {}
    count = 0
    template_flag = False
    for wiki_line in json_obj:
        wiki_info = json.loads(wiki_line)
        wiki_texts = wiki_info['text'].split("\n")
        for wiki_text in wiki_texts:
            if wiki_text.find("{{基礎情報") > -1:
                template_flag = True
                tmp_dict = {}
                continue
            if template_flag:
                if re.match("}}", wiki_text) is not None:
                    template_flag = False
                    output.update({count: tmp_dict})
                    count += 1
                    continue
                key = re.search("(?<=\|)(\s+)?[^=]+", wiki_text)
                value = re.search("(?<==)(\s+)?.+", wiki_text)
                if key is not None and value is not None:
                    tmp_dict.update({key.group(0).replace(" ", ""): value.group(0)})
        output.update({count: tmp_dict})
        count += 1
    return output


wiki_json = open("jawiki-country.json", "r")
output = get_country_information(wiki_json)
print(output)

