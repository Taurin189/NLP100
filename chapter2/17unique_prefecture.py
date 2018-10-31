# coding: utf-8

temperature_data = open("hightemp.txt", "r")

output_list = []
for line in temperature_data.readlines():
    prefecture = line.split()[0]
    if prefecture not in output_list:
        output_list.append(prefecture)
print(output_list)

temperature_data.close()