# coding: utf-8
from chapter5.morph_utils import get_chunk_dict, get_chunk_list, get_chunk_text_by_chunk_dict_till_verb

chunk_list = get_chunk_list("neko.txt.cabocha", 8)
chunk_dict = get_chunk_dict("neko.txt.cabocha", 8)
verb_dist = {}
for chunk in chunk_list:
    morph_list_list = chunk.get_morph_list_list()
    for morph_list in morph_list_list:
        if morph_list[2] == '動詞':
            verb_dist.update({chunk.get_num(): morph_list[1]})
            tmp_text = morph_list[0]
            break
for k, v in verb_dist.items():
    tmp_text = v + "\t"
    for chunk in chunk_list:
        if chunk.get_dst() == k:
            for morph_list in chunk.get_morph_list_list():
                if morph_list[2] == '助詞':
                    tmp_text += morph_list[1] + "\t"
    tmp_text = tmp_text[:-1]
    print(tmp_text)