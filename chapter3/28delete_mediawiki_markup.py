# coding: utf-8
from chapter3 import extract_template
from chapter3 import delete_markups

wiki_json = open("jawiki-country.json", "r")
output_dict = extract_template.get_country_information(wiki_json)
new_output_dict = {}
for country_index, country_dict in output_dict.items():
    tmp_dict = {}
    for key, value in country_dict.items():
        value = delete_markups.delete_emphasize_markup(value)
        value = delete_markups.delete_inner_link(value)
        if value.find("'''") > -1:
            print(value)
        tmp_dict.update({key: value})
    new_output_dict.update({country_index: tmp_dict})

print(new_output_dict)
