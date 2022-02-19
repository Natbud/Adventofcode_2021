# regular expression operations import:
import statistics as st

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
incomplete_lines = []

for i, line in enumerate(file_list):
    while any(pair in line for pair in removable_pairs):
        # now remove any removable pairs:
        for pair in removable_pairs:
            newline = line.replace(pair,'')
            line = newline

    print("line ", i+1, " after removals:", line)

    # Now find if there are any closing characters in the reduced line:
    if any(char in line for char in closing_chars):
        print("line:", i+1, "is corrupt, don't append:")
    else:
        print("no closing chars found in line:", i+1, " - kept")
        incomplete_lines.append(line)

print("Incomplete Lines saved:", incomplete_lines)

# Replace corrupt characters with their respective scores:

all_line_scores = []

for i, line in enumerate(incomplete_lines):
    line_score = 0
    # Important to iterate the line in REVERSE to get the order the closing char
    # Would be in when applied (they would be in reverse order of start characters)
    for char in reversed(line):
        # Each START character found needs the same CLOSING one to complete it
        # So can just search for each START one and assign the points for them.
        if char == "(":
            print(") 1 point added")
            line_score = (line_score * 5) + 1
        if char == "[":
            print("] 2 points added")
            line_score = (line_score * 5) + 2
        if char == "{":
            print("} 3 points added")
            line_score = (line_score * 5) + 3
        if char == "<":
            print("> 4 points added")
            line_score = (line_score * 5) + 4

    print("line", i+1, "score:", line_score)
    all_line_scores.append(int(line_score))

print("all line scores:", all_line_scores)
print("median line score:", st.median(all_line_scores))
