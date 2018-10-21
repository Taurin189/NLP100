# coding: utf-8

temperature_data = open("hightemp.txt", "r")
print(len(temperature_data.readlines()))

temperature_data.close()