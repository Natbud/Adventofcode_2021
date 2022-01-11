import statistics as st

filepath = "07_01_Test_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.read().split(",")

file_list = [line.strip() for line in file_list]
file_list = [int(i) for i in file_list[0:None]]

print(file_list)

# THIS TIME GET LARGEST NUMBER IN THE MIDDLE AND
# OTHERS ON EITHER SIDE ALTERNATELY - so larger
# numbers use least fuel?  Something like that.

file_list.sort()
mean_value = st.mean(file_list)
print("Mean Value is:", mean_value)

total_fuel = 0
for i in file_list:
    # fuel = 0
    fuel = abs(i - mean_value)

    # Use 'Guass' formula to get sum of all positions moved  when calculating fuel
    total_fuel = total_fuel + fuel


print("Total Fuel Is:", total_fuel)
