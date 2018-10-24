# coding: utf-8
import linecache

temperature_data = open("hightemp.txt", "r")
max_line = len(temperature_data.readlines())

n = int(input())
if n > max_line or n <= 0:
    print("invalid input")
    exit(0)
print(linecache.getline("hightemp.txt", n))


