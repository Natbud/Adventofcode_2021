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
p = 0
while day_count <= 256:
    for i in fish_list[p:None]:
        # THESE ARE NOT WORKING - NOT EVALUATING TRUE
        if i == 8:
            # print("fish at index:", p, " is 8")
            fish_list[p] = 1 # no new fish spawned for "8" fishes
            # print("fish_list index", p, "is now:", fish_list[p])
            p += 1
            continue
        if i == 7:
            fish_list[p] = 0
            fish_list.append(8) #spawn new "8" fish for any "7" fishes
            p += 1
            continue
        fish_list.append(i + 2)
        p += 1
    print("updated fish_list after day:", day_count, " is:", fish_list)
    day_count += 7



    #if day_count == 50 or day_count == 100 or day_count == 110 or day_count == 115 or day_count == 130 or day_count == 150:
print("Number of fish:", len(fish_list))
