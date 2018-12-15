# coding: utf-8
from chapter5.morph_utils import get_chunk_list

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
marks_count = 0

for chunk in chunk_list:
    print(chunk.to_list())