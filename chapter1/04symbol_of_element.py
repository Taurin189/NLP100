# coding: utf-8
magic_word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
magic_words = magic_word.split()
one_char_elements = [1, 5, 6, 7, 8, 9, 15, 16, 19]
iterator = 1

for word in magic_words:
    if iterator in one_char_elements:
        print(word[0])
    else:
        print(word[0:2])
    iterator += 1

