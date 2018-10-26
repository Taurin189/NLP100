# coding: utf-8

temperature_data = open("hightemp.txt", "r")

n = int(input())
i = 0
for line in temperature_data.readlines():
    if i >= n:
        break
    print(line.replace("\n", " "))
    i += 1
temperature_data.close()


