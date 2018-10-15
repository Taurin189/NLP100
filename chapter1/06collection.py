# coding: utf-8
X = "paraparaparadise"
Y = "paragraph"


def n_gram(n, word):
    n_gram_words = []
    for i in range(len(word)):
        n_gram_words.append(word[i:i+n])
    return n_gram_words

x_n_gram = n_gram(2, X)
y_n_gram = n_gram(2, Y)

print(set(x_n_gram) | set(y_n_gram))
print(set(x_n_gram) & set(y_n_gram))
print(set(x_n_gram) - set(y_n_gram))

print("se include in x n gram is " + str("se" in x_n_gram))
print("se include in y n gram is " + str("se" in y_n_gram))
