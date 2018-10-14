# coding: utf-8
magic_word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
magic_word = magic_word.replace(",", "")
magic_word = magic_word.replace(".", "")
words = magic_word.split()
pi_text = ""
for word in words:
    pi_text += str(len(word))
    if len(pi_text) == 1:
        pi_text += "."

print(pi_text)
