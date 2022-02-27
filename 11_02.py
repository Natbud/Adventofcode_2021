import numpy as np
import re as re

filepath = "11_01_Data.txt"

# using splitlines like this is good as it splits on the newline character
# which essentially removes it from each line during reading.
with open(filepath) as f:
    file_list = f.read().splitlines()

print("file_list:", file_list)

# FOLLOWING CODE TAKEN FROM DAY 9 TO GET A GRID GOING USING NUMPY:

# Get the size of file_list to help with creating numpy array of same size.
# rows:
file_list_row_len = (len(file_list))
print("file_list rows:", file_list_row_len)
# columns:
file_list_col_len = (len(file_list[0]))
print("file_list cols:", file_list_col_len)

# Create a numpy array of same size as file_list and add all zeroes:
np_grid = np.zeros((file_list_row_len,file_list_col_len))

# read in all the values from file_list into np_grid array
for r, row in enumerate(file_list):
    for d, digit in enumerate(row):
        np_grid[r][d] = digit

print("np_grid before any steps:\n", np_grid)

# GRID CREATED.

# Set number of steps to execute:
max_steps = 1000
step = 0
flashes_count = 0
while step < max_steps:
    # START A 'STEP':
    step += 1

    # Substep 1:  Increase every element in grid by 1
    for r, row in enumerate(np_grid):
        for d, digit in enumerate(row):
            np_grid[r][d] += 1

    print("step:",step, " all increased by 1:\n", np_grid)

    # print("np_grid:\n", np_grid)
    flashed_list = []

    # Substep 2: 'Flash any octopus/value greater than 9'
    # Something here to ONLY check indicies NOT in flashed_list.
    while np.any(np_grid >= 10):
    # while not np.less(np.all(np_grid), 10):
        for r, row in enumerate(np_grid):
            for d, digit in enumerate(row):
                if digit >= 10 and [r,d] not in flashed_list:
                    # add co-ordinate to flashed_list
                    flashed_list.append([r,d])
                    # element flashes - increase all 8 adjacent (incl diags) by 1:
                    # NSEW:
                    # EAST
                    if not d == 9:
                        np_grid[r][d+1] +=1
                    else:
                        pass
                    # SOUTH
                    if not r ==9:
                        np_grid[r+1][d] +=1
                    else:
                        pass
                    # WEST
                    # Buid in my own 'catch for a value on left side of board
                    # because it just loops / affects right side otherwise:
                    if d == 0:
                        pass
                    else:
                        np_grid[r][d-1] +=1
                    # NORTH
                    # And another if row is zero, loops to affect bottom of GRID
                    # so build in own catch:
                    if r == 0:
                        pass
                    else:
                        np_grid[r-1][d] +=1

                    # NORTH EAST:
                    if r == 0 or d == 9:
                        pass
                    else:
                        np_grid[r-1][d+1] +=1
                    # SOUTH EAST
                    if r == 9 or d == 9:
                        pass
                    else:
                        np_grid[r+1][d+1] +=1
                    # NORTH WEST
                    if r == 0 or d == 0:
                        pass
                    else:
                        np_grid[r-1][d-1] +=1
                    # SOUTH WEST
                    if d == 0 or r == 9:
                        pass
                    else:
                        np_grid[r+1][d-1] +=1
                    np_grid[r][d] = -100
                    flashes_count += 1
                    # print("FLASH HAPPENED\n",re.sub('[\[\]]', '', np.array_str(np_grid)))

    # Now need to FLASH any others that have reached 10 or more....recursive?
    # Add flashed positions to a list so those positions can't be flashed agian
    # While any value in np_grid > 9 AND If np_grid position is NOT on don't check list...
    # Then flash and incrase surrounding for any value greater than 9.
    print("np_grid after flashes:\n",np_grid)

    print("flashed lists step:",step,"\n", flashed_list,"\n")
    # finally set all octopuses with values greater than 9 to 0:
    for r, row in enumerate(np_grid):
        for d, digit in enumerate(row):
            # if digit > 9:
            if digit < 0:
                np_grid[r][d] = 0

    # THIS CODE IS ALL THAT IS NEEDED FOR PART 2:
    # NOW check if all elements in grid are zeroes or not:
    all_zeros = not np.any(np_grid)
    if all_zeros == True:
        print("All digits are zero after step:", step)
        exit()



    print("np_grid after zeroes added after step:", step, "\n", np_grid)

print("Total Number of Flashes in", step, "steps:", flashes_count)
