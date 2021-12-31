from collections import Counter

filepath = "03_02_Data.txt"

with open(filepath) as f:
    file_list = f.readlines()

# Input TEST Data:
# file_list = ['00100\n', '11110\n', '10110\n', '10111\n', '10101\n', '01111\n', '00111\n', '11100\n', '10000\n',
#             '11001\n', '00010\n', '01010']

Pos1 = []
Pos2 = []
Pos3 = []
Pos4 = []
Pos5 = []
Pos6 = []
Pos7 = []
Pos8 = []
Pos9 = []
Pos10 = []
Pos11 = []
Pos12 = []
first_bits = []
second_bits = []
third_bits = []
fourth_bits = []
fifth_bits = []
sixth_bits = []
seventh_bits = []
eighth_bits = []
ninth_bits = []
tenth_bits = []
eleventh_bits = []
twelfth_bits = []

ox_gen_rating_final = []
c02_scrub_rating = []

most_common = []
binary_count = []


# Function to check Oxygen Binary Number positions
def position_check(start_list, result_list, bits_list, position):
    for line in start_list:
        bits_list.append(line[position])

    print("full initial bit list:", bits_list)

    # Find the most common (0 or 1?):
    c = Counter(bits_list)
    c.most_common(1)

    if "1" in c.most_common(1)[0][0] or (bits_list.count("1")) == (bits_list.count("0")):
        print("Most Common is 1")
        # Add all numbers with 1 in first position to Pos1 list:
        for line in start_list:
            if line[position] == "1":
                result_list.append(line)
        return result_list
    else:
        print("Most Common is 0")
        # Add all numbers with 0 in first position to Pos1 list:
        for line in start_list:
            if line[position] == "0":
                result_list.append(line)
        return result_list


# FUNCTION to report OXYGEN results
def result_print(final_pos):
    # Convert Binary to Decimal and report Oxygen Generator Rating:
    ox_gen_rating_dec = int((final_pos[0]), 2)
    # print("Oxygen Generator Rating:", ox_gen_rating_dec)
    return ox_gen_rating_dec


# Code / Function for C02 SCRUBBER RATING:
def position_check_2(start_list, result_list, bits_list, position):
    for line in start_list:
        bits_list.append(line[position])

    # Find the most common (0 or 1?):
    c = Counter(bits_list)
    c.most_common(1)

    # print(c)
    # print(c.most_common(1)[0][0])

    if "1" in c.most_common(1)[0][0] or (bits_list.count("1")) == (bits_list.count("0")):
        print("Most Common is 1, so Least Common is 0")
        # Add all numbers with 0 (LEAST COMMON in first position to result_list list:
        for line in start_list:
            if line[position] == "0":
                result_list.append(line)
        return result_list
    else:
        print("Most Common is 0, so Least common is 1")
        # Add all numbers with 0 in first position to result_list list:
        for line in start_list:
            if line[position] == "1":
                result_list.append(line)
        return result_list


# Function prints C02 result
def result_print_2(final_pos):
    # Convert Binary to Decimal and report Oxygen Generator Rating:
    c02_rating_dec = int((final_pos[0]), 2)
    # print("C02 Scrubber Rating:", c02_rating_dec)
    return c02_rating_dec


def final_answer():
    # Final Answer:
    print("Oxygen Rating X C02 Scrubber Rating:", ox_gen_rating_final * c02_scrub_rating)


# Function to check binary numbers for C02
def c02_checks():
    # Clear out Reusable Variables (but keep 'first_bits' etc. as those values remain same:

    Pos1 = []
    Pos2 = []
    Pos3 = []
    Pos4 = []
    Pos5 = []
    Pos6 = []
    Pos7 = []
    Pos8 = []
    Pos9 = []
    Pos10 = []
    Pos11 = []
    Pos12 = []
    first_bits = []
    second_bits = []
    third_bits = []
    fourth_bits = []
    fifth_bits = []
    sixth_bits = []
    seventh_bits = []
    eighth_bits = []
    ninth_bits = []
    tenth_bits = []
    eleventh_bits = []
    twelfth_bits = []

    def c02_check_loop(this_list, pos_var, bit_list, position):
        print("Values Kept for Pos1:", position_check_2(this_list, pos_var, bit_list, position))

        if len(pos_var) == 1:
            global c02_scrub_rating
            c02_scrub_rating = result_print_2(pos_var)
            print("C02 Scrubber Rating Is:", c02_scrub_rating)
            # Call the Final Answer function and then exit so that remaining iterations/checks don't run.
            final_answer()
            exit()

    c02_check_loop(file_list, Pos1, first_bits, 0)
    c02_check_loop(Pos1, Pos2, second_bits, 1)
    c02_check_loop(Pos2, Pos3, third_bits, 2)
    c02_check_loop(Pos3, Pos4, fourth_bits, 3)
    c02_check_loop(Pos4, Pos5, fifth_bits, 4)
    c02_check_loop(Pos5, Pos6, sixth_bits, 5)
    c02_check_loop(Pos6, Pos7, seventh_bits, 6)
    c02_check_loop(Pos7, Pos8, eighth_bits, 7)
    c02_check_loop(Pos8, Pos9, ninth_bits, 8)
    c02_check_loop(Pos9, Pos10, tenth_bits, 9)
    c02_check_loop(Pos10, Pos11, eleventh_bits, 10)
    c02_check_loop(Pos11, Pos12, twelfth_bits, 11)


def oxygen_checks(this_list, pos_var, bit_list, position):
    # Initially this code runs to check Oxygen Binary Numbers.
    print("Values Kept for Pos1:", position_check(this_list, pos_var, bit_list, position))
    if len(pos_var) == 1:
        global ox_gen_rating_final
        ox_gen_rating_final = result_print(pos_var)
        print("Oxygen Gen Rating Is:", ox_gen_rating_final)
        c02_checks()


oxygen_checks(file_list, Pos1, first_bits, 0)
oxygen_checks(Pos1, Pos2, second_bits, 1)
oxygen_checks(Pos2, Pos3, third_bits, 2)
oxygen_checks(Pos3, Pos4, fourth_bits, 3)
oxygen_checks(Pos4, Pos5, fifth_bits, 4)
oxygen_checks(Pos5, Pos6, sixth_bits, 5)
oxygen_checks(Pos6, Pos7, seventh_bits, 6)
oxygen_checks(Pos7, Pos8, eighth_bits, 7)
oxygen_checks(Pos8, Pos9, ninth_bits, 8)
oxygen_checks(Pos9, Pos10, tenth_bits, 9)
oxygen_checks(Pos10, Pos11, eleventh_bits, 10)
oxygen_checks(Pos11, Pos12, twelfth_bits, 11)
