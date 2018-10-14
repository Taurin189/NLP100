# coding: utf-8
text1 = "パトカー"
text2 = "タクシー"

combined_text = ""

linking = ""

for (s1, s2) in zip(text1, text2):
    combined_text += (s1 + s2)
print(combined_text)