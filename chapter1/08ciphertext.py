# coding: utf-8
import re


def cipher(text):
    cipher_text = ""
    for c in text:
        if re.compile(r'[a-z]').match(c) is not None:
            cipher_text += str(219 - ord(c))
        else:
            cipher_text += c
    return cipher_text


text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
print(cipher(text))