import numpy as np

filepath = "06_01_Test_Data.txt"

with open(filepath, 'r') as f:
    file_list = f.readlines()

print("file_list:", file_list)

new_list = []

for line in file_list:
    new_list.append(line.strip())
    print("new_list:", new_list)
