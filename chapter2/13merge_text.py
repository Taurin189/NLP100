# coding: utf-8

col1_data = open("col1.txt", "r")
col2_data = open("col2.txt", "r")
col1 = []
col2 = []

for col1_line in col1_data.readlines():
    col1.append(col1_line)
for col2_line in col2_data.readlines():
    col2.append(col2_line)

with open("merged.txt", "w") as mergedfile:
    for i in range(len(col1)):
        col1[i] = col1[i].replace("\n", "")
        mergedfile.write(col1[i] + "\t" + col2[i])