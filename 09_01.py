import numpy as np

filepath = "09_01_Test_Data.txt"
#
with open(filepath) as f:
    file_list = f.read().splitlines()

print("file_list:", file_list)

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
# print("row length:", len(np_grid[0]))
low_points = []
risk_levels = []
# Now iterate to find low points:
for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        # print(digit)
        # Find "North" location data (directly above current point in dataset:
        # print("tested digit:", digit, "  north digit:", np_grid[r-1][d])

        north_digit = np_grid[r-1][d]
        # Only set west digit if digit isn't on the right edge or an error throws
        if d != np_grid.shape[1]-1:  # -1 due to 0 indexing!
            east_digit = np_grid[r][d+1]
        if r != np_grid.shape[0]-1:
            south_digit = np_grid[r+1][d]
        west_digit = np_grid[r][d-1]

        # Modifiers to correct digits if points are at the edge:
        if d == 0: # left side point
            # make west point 11 so it must be higher than current point.
            west_digit = 11
        if r == 0: # check if point is on the top row
            north_digit = 11
        if d == np_grid.shape[1]-1: # check if point is at the end (right) of a row
            east_digit = 11
        if r == np_grid.shape[0]-1: # check if point is on the bottom row.
            south_digit = 11

        print("\ndigit checked:  ", digit, "\n north digit:", north_digit)
        print("east_digit:", east_digit, "\n south digit:", south_digit)
        print("west_digit:", west_digit)

        # Now check if digit is a low point.

        if (digit < north_digit and digit < east_digit and
            digit < south_digit and digit < west_digit):
            low_points.append(digit)
            risk_levels.append(digit+1) # risk level is 1+ initial value for low point.
            print("LOW POINT FOUND")
print("low points found:", low_points)
print("risk levels:", risk_levels)
print("sum of risk levels:", sum(risk_levels))

#print("np_grid no of rows:", np_grid.shape[1])
# print("np_grid no of columns:", np_grid.shape[0])
