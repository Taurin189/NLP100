# coding: utf-8
from chapter5.morph_utils import get_chunk_list, get_chunk_dict, get_chunk_text

chunk_list = get_chunk_list("neko.txt.cabocha", 8)

for chunk in chunk_list:
    tmp_text = ""
    print(get_chunk_text(tmp_text, chunk, "neko.txt.cabocha", 8))


