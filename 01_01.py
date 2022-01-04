# AdventofCode Puzzle 1
# Wasn't working until Chris Arnott told me I had to define the compared values as ints
# They were strings and it was failing on one iteration out of 2000 (iteration 258 bizzarre!)


thefilepath = "01_01_Data.txt"
with open(thefilepath) as f:
    file_list = f.readlines()
#   print(file_list)

# Now compare each list item with the next.
count = 0

for i, j in enumerate(file_list[:-1]):

    if int(file_list[i + 1]) > int(file_list[i]):  # int   crucial in this line don't leave it as strings!

        count += 1
#        print(i, j, count)

    else:
        count = count
#        print(i, j, count)

print(count)
