# coding: utf-8

temperature_data = open("hightemp.txt", "r")

output_dict = {}
for line in temperature_data.readlines():
    prefecture = line.split()[0]
    if prefecture not in output_dict:
        output_dict.update({prefecture: 1})
    else:
        tmp_count = output_dict[prefecture]
        output_dict.update({prefecture: tmp_count + 1})
output_dict = sorted(output_dict.items(), key=lambda x:x[1], reverse=True)
for output in output_dict:
    print(output)

temperature_data.close()