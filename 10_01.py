# regular expression operations import:
import re

filepath = "10_01_Data.txt"

# using splitlines like this is good as it splits on the newline character
# which essentially removes it from each line during reading.
with open(filepath) as f:
    file_list = f.read().splitlines()

print("file_list:", file_list)

# remove adjacent pairs of openers / closers until none left
# if all chars left are openers - incomplete, if any closers remain - corrupt.
removable_pairs = ['{}','[]','<>','()']
closing_chars = ['}', ']', '>', ')']
corrupt_chars_found = []

for i, line in enumerate(file_list):
    while any(pair in line for pair in removable_pairs):
        # now remove any removable pairs:
        for pair in removable_pairs:
            newline = line.replace(pair,'')
            line = newline

    print("line ", i+1, " after removals:", line)

    # Now find the first closing character exisitng (if any)
    for char in line:
        if char in closing_chars:
            print("line:", i+1, "first corrupt char found:", char)
            corrupt_chars_found.append(char)
            break
print("Corrupt Characters Found:", corrupt_chars_found)
# Replace corrupt characters with their respective scores:
corrupt_score = 0
for p in corrupt_chars_found:
    if p == ")":
        print("3 added")
        corrupt_score += 3
    if p == "]":
        print("57 added")
        corrupt_score += 57
    if p == "}":
        print("1197 added")
        corrupt_score += 1197
    if p == ">":
        print("25137 added")
        corrupt_score += 25137

print("corrupt score:", corrupt_score)
