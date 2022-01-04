# first part same as part A - parse the data from actual data input:
# thefilepath = "G:\Hoylestore\Programming Coding Etc\Advent Of Code Puzzle Programs 2021\\01\\01_Data.txt"

# OR JUST FROM TEST DATA:

#PCSPECIALISTPC FILEPATH:
#thefilepath = "G:\Hoylestore\Programming Coding Etc\Advent Of Code Puzzle Programs 2021\\Test_Data.txt"

#DELL LAPTOP FILEPATH:
thefilepath = "01_02_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()

print(file_list)

# reads the lines in the list into an array/variable - WHY NOT QUITE SURE!
file_numbers = [int(line) for line in file_list]

#print(type(file_numbers))
#print(file_numbers)

#print(type(file_numbers[0])) #RETURNS 'INT' AS TYPE.

# Create a new set of data which has sums of 3 consecutive values from the original data, each '3'
# starts / iterates one place higher each time.

#need to set a and b and sumsofthree outside of loop:
a = 0
b = 3
sumsofthree = []

for i, j in enumerate(file_numbers[:-1]):

    threevalues = []

    #print(type(threevalues))

    #Get 3 values (dicated by 'a' and 'b' from list and read them into sumofthree variable.
    threevalues.append(file_numbers[a:b])
#    print(threevalues)
    #Check if there isn't a full group of 3 at the end of the file:
    #print("threevalues is length:", len(threevalues[0]))

    if len(threevalues[0]) < 3:
#        print("threevalues len is less than 3")
        break
    else:
        sumsofthree.append(sum(threevalues[0]))

    #print(sumsofthree)

        a += 1
        b += 1

#print(sumsofthree)



#     # NOW DO DAY_01_A Code to compare the sum of each group of three with the next.

count = 0

for i, j in enumerate(sumsofthree[:-1]):

    if int(sumsofthree[i + 1]) > int(sumsofthree[i]):  # int   crucial in this line don't leave it as strings!

        count += 1
#        print(i, j, count)

    else:
        count = count
#        print(i, j, count)

print("count is:", count)
