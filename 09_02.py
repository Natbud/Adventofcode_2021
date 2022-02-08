import numpy as np
import operator as op
from functools import reduce

filepath = "09_01_Data.txt"

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

all_basin_sizes = []

# Iterate through low points:
for low_point in low_point_positions:
    basin_checklist = []
    # set basin count to 1 as we know the starting low point is always a match....
    basin_count = 1
    # set low point co-ord values:
    row = low_point[0]
    col = low_point[1]
    print("\ncurrent low point being checked: ", low_point, "  value:", (int(np_grid[row][col])))
    # Add initial low point to basin check list
    basin_checklist.append([row,col])
    print("basin checklist before low point check:", basin_checklist, "\n\n")
    # HOW TO FIND BASIN SIZE.......
    # try/except to ignore any erros with values outside of grid dataset
    # them to 9 if so.  row 0 is a special case, loops back to last row so use
    # if condition instead for first one:

    # This while line seems to be resulting endless loop (checklist is never
    # emapty...)
    while not len(basin_checklist) == 0:

        # Now check each value in the basin_checklist:
        for check_value in basin_checklist[0:None]:
            print("current point being checked:", check_value)
            # Set row / col values for currrent checked point here:
            row = check_value[0]
            col = check_value[1]
            if row > 0:
                low_north = (int(np_grid[row-1][col]))
            else:
                low_north = 9
            try:
                low_east = (int(np_grid[row][col+1]))
            except:
                low_east = 9
            try:
                low_south = (int(np_grid[row+1][col]))
            except:
                low_south = 9
            if col > 0:
                low_west = (int(np_grid[row][col-1]))
            else:
                low_west = 9

            print("north:", low_north, "  east:", low_east, "  south:", low_south, "  west:", low_west)

                # Add co-ordinates from north, south , east , west of lowpoint to checklist
                # North

            if low_north < 9:
                # the if here,  only appends to list if not already there (stop duplicates being entered)
                if [row-1,col] not in basin_checklist:
                    basin_checklist.append([row-1,col])
                    basin_count += 1
            if low_east < 9:
                if [row,col+1] not in basin_checklist:
                    basin_checklist.append([row,col+1])
                    basin_count += 1
            if low_south < 9:
                if [row+1,col] not in basin_checklist:
                    basin_checklist.append([row+1,col])
                    basin_count += 1
            if low_west < 9:
                if [row,col-1] not in basin_checklist:
                    basin_checklist.append([row,col-1])
                    basin_count += 1

            # Change current checked value to a 9 in original np_grid array
            # so it will not be added to check list in future:
            np_grid[row][col] = 9
            print("np_grid checked point changed to 9:\n", np_grid)

            # Remove current check_value from checklist so isn't re=added as a
            # North South East or West point for a different low point in future
            # Deletes the first element in the list (the least recent added which
            # should equiate to the current one just checked as list is being traversed
            # in order values have been appended)
            del basin_checklist[0]

            print("basin checklist after current point check:", basin_checklist)
            print("basin count after current point check:", basin_count, "\n\n")

    print("**** Low point: ", low_point, " CHECK DONE, basin size of point:", basin_count, " *****\n\n\n")
    all_basin_sizes.append(basin_count)

sorted_basin_sizes = sorted(all_basin_sizes, reverse=True)
print("all_basin_sizes sorted high to low:", sorted_basin_sizes)
# using 'operator' (as op) and 'reduce' (from functools) imports to final multiply neatly:
print("largest 3 basin sizes multiplied together:", reduce(op.mul, sorted_basin_sizes[:3]))
