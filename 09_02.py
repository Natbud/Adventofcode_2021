import numpy as np

filepath = "09_01_Test_Data.txt"

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
low_points = []
risk_levels = []
low_point_positions = []  # for storing key pairs for co-ordinates of each low point.
# Now iterate to find low points:
for r, row in enumerate(np_grid):
    for d, digit in enumerate(row):
        # print(digit)
        # Find "North" location data (directly above current point in dataset:

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

        # print("\ndigit checked:  ", digit, "\n north digit:", north_digit)
        # print("east_digit:", east_digit, "\n south digit:", south_digit)
        # print("west_digit:", west_digit)

        # Now check if digit is a low point.
        if (digit < north_digit and digit < east_digit and
            digit < south_digit and digit < west_digit):
            low_points.append(digit)
            print("LOW POINT FOUND")
            # print("Low Point Digit", (int(digit)))
            # Collect low point position/co-ordinate:
            low_point_positions.append([r,d])

print("low_point_positions", low_point_positions)

basin_checklist = []
# Iterate through low points:
for low_point in low_point_positions:
    # start at 1 to account for current low point.
    basin_size = 1
    # set low point co-ord values:
    row = low_point[0]
    col = low_point[1]
    # HOW TO FIND BASIN SIZE.......
    # try/except to ignore any erros with values outside of grid dataset
    # them to 9 if so.
    print("current low point being checked: ", low_point, "  value:", np_grid[row][col])
    try:
        low_north = np_grid[row-1][col]
    except:
        low_north = 9
    try:
        low_east = np_grid[row][col+1]
    except:
        low_east = 9
    try:
        low_south = np_grid[row+1][col]
    except:
        low_south = 9
    try:
        low_west = np_grid[row][col-1]
    except:
        low_west = 9

    print("north:", low_north, "  east:", low_east, "  south:", low_south, "  west:", low_west)

        # Add north, south , east , west of lowpoint to checklist
        # North

    if low_north < 9:
        basin_checklist.append([np_grid[col-1],[row]])
