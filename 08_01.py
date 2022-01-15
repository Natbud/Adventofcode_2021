
filepath = "08_01_Data.txt"

with open(filepath, 'r') as f:    in file_list]
print(file_list)


word_lengths = []

for output in file_list[0:None]:
    for word in output.split():
        # print(word)
        word_lengths.append(len(word))

print(word_lengths)

# How to count mulitple different values in a list:
digit1 = 2
digit4 = 4
digit7 = 3
digit8 = 7
final_count = 0

for length in word_lengths:
    if length == digit1 or length == digit4 or length == digit7 or length == digit8:
        final_count += 1

print(final_count)
