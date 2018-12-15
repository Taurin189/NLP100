# coding: utf-8
from chapter5.Morph import Morph
from chapter5.Chunk import Chunk


def get_sentence_lines_by_num(file_name, num):
    sentence_lines = []
    marks_count = 0
    morph_file = open(file_name, "r")
    for word_line in morph_file:
        if marks_count == num:
            sentence_lines.append(word_line)
        if marks_count > num:
            break
        if word_line.startswith("。"):
            marks_count += 1
    return sentence_lines


def get_morph_list(file_name, num):
    morph_list = []
    morph_file = get_sentence_lines_by_num(file_name, num)
    for word_line in morph_file:
        word_line = word_line.replace("\t", ",")
        word_analysis = word_line.split(",")
        if len(word_analysis) < 9:
            continue
        tmp_morph = Morph(surface=word_analysis[0], base=word_analysis[7], pos=word_analysis[1], pos1=word_analysis[2])
        morph_list.append(tmp_morph)
    return morph_list


def get_chunk_list(file_name, num):
    chunk_list = []
    morph_file = get_sentence_lines_by_num(file_name, num)
    tmp_chunk = None
    for word_line in morph_file:
        if word_line[0].startswith("*"):
            word_analysis = word_line.split()
        else:
            word_line = word_line.replace("\t", ",")
            word_analysis = word_line.split(",")
        if word_analysis[0] == "*":
            if tmp_chunk is not None:
                chunk_list.append(tmp_chunk)
            tmp_chunk = Chunk()
            tmp_chunk.set_num(word_analysis[1])
            tmp_chunk.set_dst(word_analysis[2])
            for chunk in chunk_list:
                if word_analysis[1] == chunk.get_dst()[:-1]:
                    tmp_chunk.append_srcs(chunk.get_num())
        elif len(word_analysis) > 8:
            tmp_morph = Morph(surface=word_analysis[0], base=word_analysis[7], pos=word_analysis[1],
                              pos1=word_analysis[2])
            tmp_chunk.append_morph_list(tmp_morph)
            tmp_chunk.append_morph_list_list(tmp_morph)
    if tmp_chunk is not None:
        chunk_list.append(tmp_chunk)
    return chunk_list
