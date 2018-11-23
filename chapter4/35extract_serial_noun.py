# coding: utf-8
import re
import time
from chapter4 import dict_utils

time_start = time.time()
categorized_words = dict_utils.get_dict("neko.txt.mecab")
