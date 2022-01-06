import numpy as np

filepath = "06_01_Test_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]

# take values inbetween commas and insert into new list
fish_list = [line.split(",") for line in file_list]
# alter to alist of interger types rather than strings:
fish_list = [int(i) for i in fish_list[0][0:None]]

np_fish_list = np.array(fish_list)
print("np_fish_list:", np_fish_list)

# print("Starting fish_list", fish_list)

day_count = 1
while day_count <= 150:
    for i in range(len(np_fish_list)):
        # print("fish is:", fish_list[i])
        if np_fish_list[i] == 0:
            np_fish_list = np.append(np_fish_list, 8)
            np_fish_list[i] = 7
        np_fish_list[i] -= 1

    # print("updated fish_list after day:", day_count, " is:", np_fish_list)

    day_count += 1
    #if day_count == 50 or day_count == 100 or day_count == 110 or day_count == 115 or day_count == 130 or day_count == 150:
    print("day_count is:", day_count)

print("Number of fish:", len(np_fish_list))
