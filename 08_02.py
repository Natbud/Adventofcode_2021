
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

for digit in file_list_digits[0:None]:
    for word in digit.split():
        # print(word)
        word_length = (len(word))
        # check for 1, 4, 7 and 8 Unique number of segments for these:
        if word_length == 2:
            digit_value = 1
        if word_length == 4:
            digit_value = 4
        if word_length == 3:
            digit_value = 7
        if word_length == 7:
            digit_value = 8
        # check for 0, 6, 9 (all length 6)
        if word_length == 6 and "f" not in word:
            digit_value = 0
        if word_length == 6 and "a" not in word:
            digit_value = 6
        if word_length == 6 and "g" not in word:
            digit_value = 9

        # check for 2, 3, 5 (all length 5) - THIS ISN'T WORKING......
        matches1 = ["e", "b"]
        if word_length == 5 and all(x not in word for x in matches1):
            digit_value = 2
        matches2 = ["e", "g"]
        if word_length == 5 and all(x not in word for x in matches2):
            digit_value = 3
        matches3 = ["a", "g"]
        if word_length == 5 and all(x not in word for x in matches3):
            digit_value = 5


        print(word, digit_value)
    print("digit just done:", digit)





# print(final_count)
