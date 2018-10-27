# coding: utf-8

temperature_data = open("hightemp.txt", "r")

n = int(input())
for line in temperature_data.readlines()[-n:]:
    print(line.replace("\n", " "))
temperature_data.close()