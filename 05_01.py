import numpy as np

filepath = "05_01_Data.txt"

with open(filepath) as f:
    file_list = f.readlines()

# print(file_list, "\n")


# Set up numpy binary array for storing points/lines:
np_all_positions = np.zeros((1000, 1000))
# print(np_all_positions)

print("Processing.....")

for line in file_list:
    x = line.strip("\n").split(" -> ")
    split_x = (x[0].split(","), x[1].split(","))
    # print("split x is:", split_x)

    x1 = int(split_x[0][0])
    x2 = int(split_x[1][0])
    y1 = int(split_x[0][1])
    y2 = int(split_x[1][1])
    y = (y1, y2)
    # print("\n y is:", y)

    # print("\n line:", line, "\n")
    # print("x: ", x, "  x1:", x1, "  x2:", x2, "\n\n")
    # print("x: ", x, "  y1:", y1, "  y2:", y2, "\n\n")

    all_lines = []
    # check if co-ordinates will form staright line.......
    # check horizontal lines first:
    if x1 == x2:
        d = (int(min(y1, y2)))
        # print("\n\n d is:", d)
        # print("max y is:", (int(max(y1, y2))))
        # print("y1:", y1, "  y2:", y2)
        line_of_points = []

        while not d > (int(max(y1, y2))):
            point = (list(map(int, (x1, d))))
            # print("\n x Point:", point)
            # print("\n x Point[0]", point[0])
            line_of_points.append(point)
            # Increment numpy zeros array at correct location:
            np_all_positions[point[1]][point[0]] += 1
            # print("\n d is:", d)
            d += 1
            # print("Line_of_points:", line_of_points)
            # print("\n", np_all_positions)

    # check vertical lines:
    if y1 == y2:
        d = (int(min(x1, x2)))
        line_of_points = []
        while not d > (int(max(x1, x2))):
            point = (list(map(int, (d, y1))))
            # print("\n y Point:", point)
            # print("\n y Point[0]", point[0])
            line_of_points.append(point)
            # Increment numpy zeros array at correct location:
            np_all_positions[point[1]][point[0]] += 1
            d += 1
            # print("Line_of_points:", line_of_points)

# print("\n", np_all_positions)


# Finally calculate the number of values which are 2 or more...
# (greater than 1)

# Return list of 1 values tallying each value above 1 in the array:
danger_areas = sum(i >= 2 for i in np_all_positions)
# print("\n\n Danger areas tally:", danger_areas)

# Count up those 1 values from previous array to get total:
danger_count = sum(danger_areas[0:None])
print("\n Danger areas count:", danger_count)
