# coding: utf-8

temperature_data = open("hightemp.txt", "r")
replaced_data = []
for temperature_line in temperature_data.readlines():
    replaced_data.append(temperature_line.replace("\t", " "))
print(replaced_data)

temperature_data.close()
