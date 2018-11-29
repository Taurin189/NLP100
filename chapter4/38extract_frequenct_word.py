# coding: utf-8
from chapter4 import dict_utils
import matplotlib as mpl
import matplotlib.pyplot as plt

frequency_words_dict = dict_utils.get_frequency_word_dict("neko.txt.mecab")
frequency_words_dict = sorted(frequency_words_dict.items(), key=lambda x: -x[1])
print(frequency_words_dict)

frequent_top_10_words = {}
frequent_top_10_words_list = []
x = []
y = []
count = 0
for val in frequency_words_dict:
    frequent_top_10_words.update({list(val)[1]: list(val)[0]})
    print(list(val))
    x.append(list(val)[0])
    y.append(list(val)[1])
    count += 1
    if count >= 100:
        break

font = {"family": "AppleGothic"}
mpl.rc('font', **font)

plt.plot(x, y)
plt.show()