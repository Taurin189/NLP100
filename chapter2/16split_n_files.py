# coding: utf-8
import math

temperature_data = open("hightemp.txt", "r")
line_count= len(temperature_data.readlines())
temperature_data.close()
n = int(input())
one_file_lines = math.floor(line_count / n)

for i in range(n):
    with open("hightemp." + str(i + 1) + ".txt", "w") as output:
        temperature_data = open("hightemp.txt", "r")
        for line in temperature_data.readlines()[i*one_file_lines: (i+1)*one_file_lines]:
            output.write(line)
        temperature_data.close()
