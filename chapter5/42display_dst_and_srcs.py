# coding: utf-8
from chapter5.morph_utils import get_chunk_list, get_chunk_dict

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 8)


def get_chunk_text(text, chunk):
    for morph in chunk.get_morph_list():
        text += morph.surface
    if chunk.get_dst() == -1:
        return text
    if chunk.get_dst() not in chunk_dict.keys():
        return text
    text += "\t"
    next_chunk = chunk_dict[chunk.get_dst()]
    text = get_chunk_text(text, next_chunk)
    return text


for chunk in chunk_list:
    tmp_text = ""
    print(get_chunk_text(tmp_text, chunk))


