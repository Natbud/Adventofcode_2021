import numpy as np

filepath = "11_01_Small_Test_Data.txt"

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

print("np_grid:\n", np_grid)

# GRID CREATED.

# START A 'STEP':
# Substep 1:  Increase every element in grid by 1
for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        np_grid[r][d] += 1

print("np_grid:\n", np_grid)

# Substep 2: 'Flash any octopus/value greater than 9'
for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        if np_grid[r][d] > 9:
            # element flashes - increase all 8 adjacent (incl diags) by 1:
            # NSEW:
            np_grid[r][d+1] +=1
            np_grid[r+1][d] +=1
            np_grid[r][d-1] +=1
            np_grid[r-1][d] +=1
            # DIAGS:
            np_grid[r-1][d+1] +=1
            np_grid[r+1][d+1] +=1
            np_grid[r-1][d-1] +=1
            np_grid[r+1][d-1] +=1

            # finally set current octopus to 0:
            np_grid[r][d] = 0

print("np_grid:\n", np_grid)
