# coding: utf-8
import json
from chapter3 import extract_template


wiki_json = open("jawiki-country.json", "r")
output_dict = extract_template.get_country_information(wiki_json)

for k, v in output_dict.items():
    print(k, v)
    # for k2, v2 in v.items():
    #     print(k2, v2)
# output = []
# for wiki_line in wiki_json:
#     wiki_info = json.loads(wiki_line)
#     wiki_texts = wiki_info['text'].split("\n")
#     for wiki_text in wiki_texts:
#         wiki_text = wiki_text.replace("'''''", "")
#         wiki_text = wiki_text.replace("'''", "")
#         wiki_text = wiki_text.replace("''", "")
#         output.append(wiki_text)
#
# for line in output:
#     print(line)