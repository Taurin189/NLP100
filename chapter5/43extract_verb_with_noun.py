# coding: utf-8
from chapter5.morph_utils import get_chunk_dict, get_chunk_list, get_chunk_text_by_chunk_dict_till_verb

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 8)

for chunk in chunk_list:
    morph_list = chunk.get_morph_by_case('名詞')
    for morph in morph_list:
        tmp_text = ""
        print(get_chunk_text_by_chunk_dict_till_verb(tmp_text, chunk, chunk_dict))