import numpy as np

filepath = "11_01_Test_Data.txt"

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
max_steps = 100
step = 0

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
    # while not np.all(np_grid < 10):
    # while not np.less(np.all(np_grid), 10):
    for r, row in enumerate(np_grid):
        for d, digit in enumerate(row):
            if digit >= 10 and [r,d] not in flashed_list:
                # add co-ordinate to flashed_list
                flashed_list.append([r,d])
                # element flashes - increase all 8 adjacent (incl diags) by 1:
                # NSEW:
                try:
                    np_grid[r][d+1] +=1
                except:
                    pass
                try:
                    np_grid[r+1][d] +=1
                except:
                    pass
                try:
                    np_grid[r][d-1] +=1
                except:
                    pass
                try:
                    np_grid[r-1][d] +=1
                except:
                    pass
                try:
                # DIAGS:
                    np_grid[r-1][d+1] +=1
                except:
                    pass
                try:
                    np_grid[r+1][d+1] +=1
                except:
                    pass
                try:
                    np_grid[r-1][d-1] +=1
                except:
                    pass
                try:
                    np_grid[r+1][d-1] +=1
                except:
                    pass


    # Now need to FLASH any others that have reached 10 or more....recursive?
    # Add flashed positions to a list so those positions can't be flashed agian
    # While any value in np_grid > 9 AND If np_grid position is NOT on don't check list...
    # Then flash and incrase surrounding for any value greater than 9.
    print("np_grid after flashes:\n",np_grid)

    print("flashed lists step:",step,"\n", flashed_list,"\n")
    # finally set all octopuses with values greater than 9 to 0:
    for r, row in enumerate(np_grid):
        for d, digit in enumerate(row):
            if digit > 9:
                np_grid[r][d] = 0
            # now make sure that

    print("np_grid after zeroes added after step:", step, "\n", np_grid)
