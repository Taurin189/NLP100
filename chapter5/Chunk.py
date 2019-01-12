# coding: utf-8


class Chunk:
    def __init__(self):
        self.morph_list = []
        self.morph_list_list = []
        self.num = 0
        self.dst = 0
        self.srcs_list = []

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def get_morph_list(self):
        return self.morph_list

    def get_morph_by_case(self, case):
        morph_list_of_case = []
        for morph in self.morph_list:
            if morph.pos == case:
                morph_list_of_case.append(morph)
        return morph_list_of_case

    def append_morph_list(self, morph):
        self.morph_list.append(morph)

    def append_morph_list_list(self, morph):
        self.morph_list_list.append(morph.to_list())

    def get_morph_list_list(self):
        return self.morph_list_list

    def get_dst(self):
        return self.dst

    def set_dst(self, dst):
        self.dst = dst

    def append_srcs(self, srcs):
        self.srcs_list.append(srcs)

    def to_list(self):
        return [self.num, self.dst, self.srcs_list, self.morph_list_list]