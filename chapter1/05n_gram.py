# coding: utf-8


def n_gram(n, word):
    n_gram_words = []
    for i in range(len(word)):
        n_gram_words.append(word[i:i+n])
    return n_gram_words

word = "I am an NLPer"
print(n_gram(2, word))
