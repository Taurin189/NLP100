# coding: utf-8
from chapter3 import extract_template

wiki_json = open("jawiki-country.json", "r")
output_dict = extract_template.get_country_information(wiki_json)

print(output_dict)