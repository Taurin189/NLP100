# coding: utf-8

temperature_data = open("hightemp.txt", "r")
col1 = []
col2 = []

for temperature_line in temperature_data.readlines():
    tmp_line_cols = temperature_line.split("\t")
    col1.append(tmp_line_cols[0])
    col2.append(tmp_line_cols[1])
with open("col1.txt", "w") as col1file:
    for col1_item in col1:
        col1file.write(col1_item + "\n")
with open("col2.txt", "w") as col2file:
    for col2_item in col2:
        col2file.write(col2_item + "\n")
