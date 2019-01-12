# coding: utf-8
from chapter5.morph_utils import get_chunk_dict, get_chunk_list

chunk_list = get_chunk_list("neko.txt.cabocha", 4)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 4)
# for chunk in chunk_list:
#     print(chunk.to_list())
verb_dist = {}
subject_dict = {}
text_dict = {}

for chunk in chunk_list:
    morph_list = chunk.get_morph_by_case('動詞')
    for morph in morph_list:
        verb_dist.update({chunk.get_num(): morph.base})
        tmp_text = morph_list[0]
        break

for k, v in verb_dist.items():
    tmp_text = v + "\t"
    for chunk in chunk_list:
        if chunk.get_dst() == k:
            morph_list = chunk.get_morph_by_case('助詞')
            for morph in morph_list:
                tmp_text += morph.base + "\t"
            subject_dict.update({chunk.get_dst(): chunk.get_num()})
    for chunk in chunk_list:
        if chunk.get_dst() == k:
            for morph in chunk.get_morph_list():
                tmp_text += morph.surface
            tmp_text += "\t"
    tmp_text = tmp_text[:-1]

    print(tmp_text)