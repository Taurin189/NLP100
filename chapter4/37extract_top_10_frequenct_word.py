# coding: utf-8
from chapter4 import dict_utils
import pandas as pd
import matplotlib.pyplot as plt

frequency_words_dict = dict_utils.get_frequency_word_dict("neko.txt.mecab")
frequency_words_dict = sorted(frequency_words_dict.items(), key=lambda x: -x[1])
print(frequency_words_dict)

frequent_top_10_words = {}
count = 0
for val in frequency_words_dict:
    frequent_top_10_words.update({list(val)[0]: list(val)[1]})
    print(list(val))
    count += 1
    if count >= 10:
        break
df = pd.DataFrame.from_dict(frequent_top_10_words)
data = df['score'].tolist()
data = df.iloc[:0]
plt.hist(frequent_top_10_words)
plt.show()