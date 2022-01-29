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


# Iterate through low points:
for low_point in low_point_positions:
    basin_size = 0
    # set low point co-ord values:
    row = low_point[0]
    col = low_point[1]
    # start traversal to find basin size:
    # RIGHT FROM LOW POINT:
    for row_val in np_grid[row:row+1]:
        print("starting low point right traversal:")
        for col_val in row_val[col:None]:
            if col_val < 9:
                print("right col-val < 9 current row:", (int(col_val)))
            else:
                # MOVE ON TO LEFT LOW POINT HERE:
                print("low point horizontal right explore finished")
                break
        # LEFT FROM LOW POINT:
        print("now starting left horiz traversal:")
        # col -1 used to avoid re-counting the inital value at low point
        for col_val in row_val[col-1::-1]:
            if col_val < 9:
                print("left col-val < 9 current row:", (int(col_val)))
            else:
                # MOVE ON TO LEFT LOW POINT HERE:
                print("low point horizontal left explore finished")
                break
