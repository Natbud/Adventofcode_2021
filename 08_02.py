
filepath = "08_01_Test_Data.txt"

with open(filepath, 'r') as f:
    file_list = f.readlines()

file_list = [line.strip("\n") for line in file_list]
print(file_list)

# Get digits codes from 1st half of each line:
file_list_digits = [line.split("|")[0].strip() for line in file_list]
print(file_list_digits)

# Get output code from 2nd half of each line:
file_list_output = [line.split("|")[1].strip() for line in file_list]
print(file_list_output)



word_lengths = []

for output in file_list_output[0:None]:
    for word in output.split():
        # print(word)
        word_lengths.append(len(word))

# print(word_lengths)

# How to count mulitple different values in a list:
digit1 = 2
digit4 = 4
digit7 = 3
digit8 = 7
digit_value = 0

for length in word_lengths:
    # check for 1, 4, 7 and 8 Unique number of segments for these:
    if length == 2
    digit_value = 1
    if length == 4
    digit_value = 4
    if length == 3
    digit_value = 7
    if length == 7
    digit_value = 8

 




    or length == 4 or length == 3 or length == 7:



print(final_count)
