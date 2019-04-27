# coding: utf-8


def include_stop_word(stop_word):
    stop_word_file = open("stop_word.txt", "r")
    stop_word_list = []

    for word_line in stop_word_file:
        stop_word_list.append(word_line)

    if stop_word in stop_word_list:
        return True
    return False


word = input()
print(include_stop_word(word))



