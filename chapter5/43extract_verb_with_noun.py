# coding: utf-8
from chapter5.morph_utils import get_chunk_dict, get_chunk_list, get_chunk_text

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 8)

for chunk in chunk_list:
    morph_list_list = chunk.get_morph_list_list()
    for morph_list in morph_list_list:
        if morph_list[2] == '名詞':
            tmp_text = ""
            print(get_chunk_text(tmp_text, chunk, "neko.txt.cabocha", 8))