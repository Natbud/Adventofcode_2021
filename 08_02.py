
filepath = "08_01_Test_Data.txt"

with open(filepath, 'r') as f:
    file_list = f.readlines()

file_list = [line.strip("\n") for line in file_list]
print(file_list)

# Get digits codes from 1st half of each line:
global file_list_digits
file_list_digits = [line.split("|")[0].strip() for line in file_list]
print(file_list_digits)

# Get output code from 2nd half of each line:
global file_list_output
file_list_output = [line.split("|")[1].strip() for line in file_list]
print(file_list_output)

word_lengths = []
digit_word_list = []
# index = 0
#Had to add addtionional loop so code would do one line only at a time:

for index, p in enumerate(file_list):

    for word in file_list_digits[index].split():
        # print("word:", word)
        word_length = (len(word))
        # print("word_length", word_length)
        # check for 1, 4, 7 and 8 Unique number of segments for these:
        if word_length == 2:
            digit_value = 1
            digit1_word = word
            digit_word_list.append(''.join(sorted(digit1_word)))
            print(word, "digit_value:", digit_value)
            # print("digit1_word:", digit1_word)
        if word_length == 4:
            digit_value = 4
            digit4_word = word
            digit_word_list.append(''.join(sorted(digit4_word)))
            print(word, "digit_value:", digit_value)
        if word_length == 3:
            digit_value = 7
            digit7_word = word
            digit_word_list.append(''.join(sorted(digit7_word)))
            print(word, "digit_value:", digit_value)
        if word_length == 7:
            digit_value = 8
            digit8_word = word
            digit_word_list.append(''.join(sorted(digit8_word)))
            print(word, "digit_value:", digit_value)

    # Need a separate loop the same for next bit (so can establish digit 1 word above
    # before proceeding)
    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 1 - Check for digit 6
        if  word_length == 6:
            if digit1_word[0] not in word or digit1_word[1] not in word:
            # print("word length is", word_length)
                digit_value = 6
                digit6_word = word
                digit_word_list.append(''.join(sorted(digit6_word)))
                print(word, "digit_value:", digit_value)
                # Now get MISSING segment lettername:
                # Way to GET DIFFERENCE OF TWO STRINGS using replace:
                digit6_missing = ""
                for char in digit8_word: #The one with all segements in....
                    if char not in digit6_word:
                        digit6_missing = digit6_missing + char
                # print("digit6_word:", digit6_word)
                # print("digit8_word:", digit8_word)
                # print("digit6_missing:", digit6_missing)

    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 2 - Check for digit 3
        if (word_length == 5 and
            digit1_word[0] in word and
            digit1_word[1] in word):
            # print("word length is", word_length)
            digit_value = 3
            digit3_word = word
            digit_word_list.append(''.join(sorted(digit3_word)))
            print(word, "digit_value:", digit_value)
            # Now find which characters are MISSING from digit 3
            # Way to GET DIFFERENCE OF TWO STRINGS using replace:
            digit3_missing = ""
            for char in digit8_word:
                if char not in digit3_word:
                    digit3_missing = digit3_missing + char
            # print("digit3_word:", digit3_word)
            # print("digit8_word:", digit8_word)
            # print("digit3_missing:", digit3_missing)

    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 3 - Check for digit 9 (one of the missing characters from 3 missing here too...)
        if word_length == 6:
            if digit3_missing[0] not in word or digit3_missing[1] not in word:
                digit_value = 9
                digit9_word = word
                print(word, "digit_value:", digit_value)
                # Now get MISSING segment lettername:
                # Way to GET DIFFERENCE OF TWO STRINGS using replace:
                digit9_missing = ""
                for char in digit8_word: #The one with all segements in....
                    if char not in digit9_word:
                        digit9_missing = digit9_missing + char
                # print("digit9_word:", digit9_word)
                # print("digit8_word:", digit8_word)
                # print("digit9_missing:", digit9_missing)

    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 4 - Check for digit 0 (missing letter different to those missing in 6 and 9)
        if word_length == 6:
            if digit6_missing[0] in word and digit9_missing[0] in word:
                digit_value = 0
                digit0_word = word
                digit_word_list.append(''.join(sorted(digit0_word)))
                print(word, "digit_value:", digit_value)

    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 5 - Check for digit 5 (missing letters same as those missing in 6 and 9)
        if word_length == 5:
            if digit6_missing[0] not in word and digit9_missing[0] not in word:
                digit_value = 5
                digit5_word = word
                digit_word_list.append(''.join(sorted(digit5_word)))
                print(word, "digit_value:", digit_value)

    for word in file_list_digits[index].split():
        word_length = (len(word))
        # RULE 6 - Check for digit 2 (2 letters missing that are present in 5)
        if word_length == 5:
            # Calculate missing segments first:
            digit2_missing = ""
            for char in digit8_word: #The one with all segements in....
                if char not in word:
                    digit2_missing = digit2_missing + char
            # print("digit2_word:", word)
            # print("digit8_word:", digit8_word)
            # print("digit2_missing:", digit2_missing)
            if digit2_missing[0] in digit5_word and digit2_missing[1] in digit5_word:
                digit_value = 2
                digit2_word = word
                digit_word_list.append(''.join(sorted(digit2_word)))
                print(word, "digit_value:", digit_value)

    # NOW work out the digits of the file_list_output
    # Read A-Z sorted - digit words into a list:
    print("digit_word_list:", digit_word_list)

    # print("file_list_output", file_list_output)

output_result_list = []


for element in file_list_output[index].split():
    print (element, "checked")
    for i in range(len(digit_word_list)):
        if ''.join(sorted(element)) == digit_word_list[i]:
            output_result_list.append(i)

print("output_result_list:", output_result_list)

# SUm the output result list:
sum_output_result_list = sum(output_result_list)
print(sum_output_result_list)


    # index += 1













print("digit (line) just done:", file_list_digits[index].split())





# print(final_count)
