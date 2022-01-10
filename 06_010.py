import numpy as np

filepath = "06_01_Test_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]

# take values inbetween commas and insert into new list
fish_list = [line.split(",") for line in file_list]
# alter to alist of interger types rather than strings:
fish_list = [int(i) for i in fish_list[0][0:None]]

print("Starting fish_list", fish_list)

day_count = 1
while day_count <= 21:
    for i in range(len(fish_list)):
        # print("fish is:", fish_list[i])
        if fish_list[i] == 0:
            fish_list.append(8)
            fish_list[i] = 7
        fish_list[i] -= 1
    print("updated fish_list after day:", day_count, " is:", fish_list)
    day_count += 1

print("Number of fish:", len(fish_list))
