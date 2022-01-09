import statistics as st

filepath = "07_01_Data.txt"
with open(filepath, 'r') as f:
    file_list = f.read().split(",")

file_list = [line.strip() for line in file_list]
file_list = [int(i) for i in file_list[0:None]]

print(file_list)

file_list.sort()
median_value = st.median(file_list)

print("Median Value is:", median_value)

total_fuel = 0
for i in file_list:
    # fuel = 0
    fuel = abs(i - median_value)
    total_fuel = total_fuel + fuel


print("Total Fuel Is:", total_fuel)
