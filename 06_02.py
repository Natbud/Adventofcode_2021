import numpy as np

filepath = "06_01_Test_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]

# take values inbetween commas and insert into new list
fish_list = [line.split(",") for line in file_list]
# alter to alist of interger types rather than strings:
fish_list = [int(i) for i in fish_list[0][0:None]]

# np_fish_list = np.array(fish_list)
# fish_dict = {fish_list[0][i]: fish_list[0][i+1] for i in range(0, len(fish_list), 2)}

#function to convert list to dictionary - NOT WORKING! only writes one value.
# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct

# # TRYING DICTIONARY APPROACH - NOT WORKING.
# fish_dict = {fish for fish in fish_list}
# print("fish_dict:", fish_dict)
# for fish in fish_dict:
#     print(fish)

print("Starting fish_list", fish_list)

day_count = 0
while day_count <= 21:
    for i in fish_list[0:None]:
        # THESE ARE NOT WORKING - NOT EVALUATING TRUE? OR ASSIGNMENT NOT WORKING>
        if fish_list[i] == 8:
            fish_list[i] = 1 # no new fish spawned for "8" fishes
        if fish_list[i] == 7:
            fish_list[i] = 0
            fish_list.append(8) #spawn new "8" fish for any "7" fishes
        fish_list.append(i + 2)
    day_count += 7
    print("updated fish_list after day:", day_count, " is:", fish_list)


    #if day_count == 50 or day_count == 100 or day_count == 110 or day_count == 115 or day_count == 130 or day_count == 150:
    print("day_count is:", day_count)

print("Number of fish:", len(fish_list))
