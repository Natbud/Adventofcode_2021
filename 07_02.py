import statistics as st
import math

filepath = "07_01_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.read().split(",")

file_list = [line.strip() for line in file_list]
file_list = [int(i) for i in file_list[0:None]]

# print(file_list)

# THIS TIME GET LARGEST NUMBER IN THE MIDDLE AND
# OTHERS ON EITHER SIDE ALTERNATELY - so larger
# numbers use least fuel?  Something like that.

file_list.sort()
print(file_list)
mean_value = math.floor(st.mean(file_list)) #round - roudns to a whole number
print("Mean Value is:", mean_value)

total_fuel = 0
for i in file_list:
    # fuel = 0
    print("crab:", i)
    positions_moved = abs(i - mean_value)
    print("positions moved:", positions_moved)

    # Use 'Guass' formula to get sum of all positions moved  when calculating fuel:
    # Getting the 'average' of the 1st and last number and multiplyting it by
    # the number of integers.
    fuel = (positions_moved * ((positions_moved +1) / 2))

    print("fuel used:", round(fuel))
    total_fuel = total_fuel + fuel


print("Total Fuel Is:", round(total_fuel))
