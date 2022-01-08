import numpy as np
from collections import defaultdict

filepath = "06_01_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.readlines()
    file_list = [line.strip() for line in file_list]

# take values inbetween commas and insert into new list
fish_list = [line.split(",") for line in file_list]
# alter to alist of interger types rather than strings:
fish_list = [int(i) for i in fish_list[0][0:None]]


# DICTIONARY APPROACH:

fish_dict = {}     # creates new empty DICTIONARY works like an array

# ENTER INITIAL VALUES / FISH INTO DICTIONARY:
# Setting the value of fish as 'keys' in dictionary - so 0 - 8 will be potential keys.
# The 'key' will be the fishes 'timer', the associated 'value' will be the number of fish with that timer
# This will keep a 'count' of how many fish have each timer value as code progresses.
for i in fish_list:
    if i not in fish_dict:    # check if the current 'fish' is already a 'key' in dict.
        fish_dict[i] = 0      # sets up an entry in dictionary with key 'i' and value 0
    fish_dict[i] += 1         # if key was there already increment it's associated value by 1 because
                              # i've just added another fish with the same 'key'.

    print(fish_dict)


# CHANGE NUMBER OF FISH WITH EACH 'TIMER' (KEY) EVERY day

days = 256

for d in range(days):

    updated_fishdict = defaultdict(int)                  # This is a 2nd temporary dictonary which doesn't throw a 'key error' if it doens't already have
                                                         # the key you are trying to alter/edit/write to.   Using defaultdict(int) means that if there is
                                                         # no key, it will assign 0 by default - so we can use this to oru advantage.

    for fish_timer, fish_count in fish_dict.items():     # .items returns both key and value pair - here assigned to _fish_timer and fish_count.
        if fish_timer == 0:                              #  Get all '0' fish that need to spawa new ones.
            updated_fishdict[6] += fish_count            #  Increments the number of fish with key (timer) "6" by the current fish_count (from the 0 fish)
            updated_fishdict[8] += fish_count            #  Increments the same number of '8' new spawned fishes (same number as fish_count)
        else:
            updated_fishdict[fish_timer-1] += fish_count     #  Moves the current 'fish_count' to the key (timer) below in the temporary dictionary.

        fish_dict = updated_fishdict                     # Update the main list with the values from the temp one.

print("Number of fish:", (sum(fish_dict.values())))




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
