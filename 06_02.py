import numpy as np

filepath = "06_01_Test_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]

# take values inbetween commas and insert into new list
fish_list = [line.split(",") for line in file_list]
# alter to alist of interger types rather than strings:
fish_list = [int(i) for i in fish_list[0][0:None]]


# DICTIONARY APPROACH:

fish_dict = {}     # creates new empty DICTIONARY works like an array

#Setting the value of fish as 'keys' in dictionary - so 0 - 8 will be potential keys.
# The 'key' will be the fishes 'timer', the associated 'value' will be the number of fish with that timer
# This will keep a 'count' of how many fish have each timer value as code progresses.
for i in fish_list:
    if i not in fish_dict:    # check if the current 'fish' is already a 'key' in dict.
        fish_dict[i] = 0      # sets up an entry in dictionary with key 'i' and value 0
    fish_dict[i] += 1         # if key was there already increment it's associated value by 1 because
                              # i've just added another fish with the same 'key'.

    print(fish_dict)




print("Number of fish:", len(fish_list))



# 7 DAY CYCLE APPROACH - GOT BOGGED DOWN IN THIS!!!
# print("Starting fish_list", fish_list)
#
# day_count = 0
# p = 0
# while day_count <= 256:
#     for i in fish_list[p:None]:
#         # THESE ARE NOT WORKING - NOT EVALUATING TRUE
#         if i == 8:
#             print("fish at index:", p, " is 8")
#             fish_list[p] = 1 # no new fish spawned for "8" fishes
#             print("fish_list index", p, "is now:", fish_list[p])
#
#             continue
#         if i == 7:
#             fish_list[p] = 0
#             fish_list.append(8) #spawn new "8" fish for any "7" fishes
#             fish_list[p] = 6
#
#             continue
#         fish_list.append(i + 2)
#
#     print("updated fish_list after day:", day_count, " is:", fish_list)
#     day_count += 7



    #if day_count == 50 or day_count == 100 or day_count == 110 or day_count == 115 or day_count == 130 or day_count == 150:
