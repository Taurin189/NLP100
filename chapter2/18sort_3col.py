# coding: utf-8

temperature_data = open("hightemp.txt", "r")

output_dict = {}
for line in temperature_data.readlines():
    line_list = line.split("\t")
    output_dict.update({line: float(line_list[2])})

output_dict = sorted(output_dict.items(), key=lambda x:x[1])
for output in output_dict:
    print(output[0].replace("\n", ""))
temperature_data.close()
