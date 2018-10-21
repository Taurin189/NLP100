# coding: utf-8

import random

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = text.split()


def typoglycemia(word):
    if len(word) < 4:
        return word
    list_order = list(range(1, len(word) - 1))
    random.shuffle(list_order)
    old_word = list(word)
    new_word = old_word[0]
    for i in range(0, len(word) - 2):
        new_word += old_word[list_order[i]]
    new_word += old_word[len(word) - 1]
    return new_word

changed_text = ""
for word in words:
    changed_text += typoglycemia(word) + " "
changed_text = changed_text[:-1]

print(changed_text)
