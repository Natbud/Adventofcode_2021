import numpy as np

filepath = "04_02_Data.txt"
#
with open(filepath) as f:
    file_list = f.readlines()

# file_list = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n', '\n', '22 13 17 11  0\n',
#              ' 8  2 23  4 24\n', '21  9 14 16  7\n', ' 6 10  3 18  5\n', ' 1 12 20 15 19\n', '\n', ' 3 15  0  2 22\n',
#              ' 9 18 13 17  5\n', '19  8  7 25 23\n', '20 11 10 24  4\n', '14 21 16 12  6\n', '\n', '14 21 17 24  4\n',
#              '10 16 15  9 19\n', '18  8 23 26 20\n', '22 11 13  6  5\n', ' 2  0 12  3  7']


# get first line to separate out random numbers:
called_numbers = (list(map(int, file_list[0].strip().split(','))))  # returns a list with elements converted to integers

# split whole file by paragraph (each list element is now a paragraph:
with open(filepath) as f:
    paragraphs = f.read().split("\n\n")

f = 1  # start from 1 here not 0 as we will slice to skip first line of input and go straight to board 1.
for i in paragraphs[1:]:  # [1:] bit 'slices' and tells to start at 1 not 0 so skips first iteration
    # print("board", f, "\n", i)
    f += 1

# PUT ALL BOARDS INTO A 3D NESTED ARRAY so all board data is in a single data structure.:

allboards = []

for n, paragraph in enumerate(paragraphs[1: None]):  # enumerate returns both value itself and also position not.
    twod_board = []

    for line in paragraph.split("\n"):
        # Next, .strip removes any unwanted whitespace from teh start and end of the line.  split separates the elements
        # by whitespace within the line.
        twod_board.append(list(map(int, line.strip().split())))
    # or this way would do the same:
    # twod_board.append([ int(i) for i in line.strip().split()])

    # Now Do something with twod_board (and 'n' if you like) - append to a new list/variable for later use:
    allboards.append(twod_board)

# print("\nallboards:\n", allboards)

# print("\n called_numbers:\n", called_numbers, "\n")

# Initialise various info about boards, rows etc as global variables:
all_positions = []
board_positions = []

# Calculate lengths of various required things:
allboards_length = len(allboards)
rowcount = len(paragraph.split("\n"))
row_length = len(paragraph.split("\n")[0].split())


# Set up a linked binary 3d array to store flagged called number positions: **NOT WORKING!!**
def vanilla_array_attempt():
    # Initial setup of an array holding binary numbers to 'flag' matches when found
    # THIS IS NOT WORKING!!! Duplicates values between each board when one is populated!

    for q in range(rowcount):
        board_positions.append([0] * row_length)

    # print("board_positions:\n", board_positions, "\n")

    for p in range(allboards_length):
        all_positions.append(board_positions)

    # print("all_positions:", all_positions)
    return ()




# Create a NUMPY ARRAY for the binary linked flagged positions of called numbers instead:

np_all_positions = np.zeros((allboards_length, 5, 5))

# print("\n np_all_positions:\n", np_all_positions)

# ITERATE THROUGH ALL DATA AND PERFORM CHECKS - 4 NESTED LOOPS REQUIRED
# 1 loop to iterate numbers_called, the other 3 to iterate through the 3 levels of 'allboards'

called_number = []
winning_board = []

print("Processing please wait....")

def check_for_match():
    global called_number, p
    global winning_board
    win_list = [] # to collect record of checked boards

    for called_number in called_numbers[0: None]:

        for (a, board) in enumerate(allboards[0: None]):

            for (b, row) in enumerate(board[0: None]):

                for (c, element) in enumerate(row[0: None]):
                    
                    # Allocate '1' value on binary scoreboard for the matched position / board:
                    if element == called_number:
                        # print("Match found at:", a, b, c, "for called number:", called_number)
                        np_all_positions[a][b][c] = 1
                        

                        # Now check binary scoreboard for any winning boards by checking full rows and full columns in each board.
                        
                        # Encapsulate both row and columns checks in a master for loop length of all boards in bineary scoreboard:
                        for p in range(len(np_all_positions)):

                            #Only proceed for boards that have not yet won
                            if p not in win_list:

                                # Check if any rows are full yet:
                                if all(q > 0 for q in np_all_positions[p][b]) == True:
                                    # print("\n\nvalue of p is:", p)
                                    # print("Board:", p + 1, "row:", b, "has a full row")
                                    winning_board = p
                                    win_list.append(p)
                                    # print("item added to win_list:\n", win_list)
                                    # print("win_list length is:", len(win_list))
                                    # print(np_all_positions)
                                    if len(win_list) == allboards_length:
                                        # print("win_list length contains all boards and is:", len(win_list))
                                        return ()
                                 
                                #As p has been updated - re assert only to proceed for boards that have not yet won.
                                if p not in win_list:

                                   # Check if any columns are full yet:
                                    if (np_all_positions[p] == 1).all(axis=0).any():
                                        # print("value of a is:", a)
                                        # print("\n\nBoard:", p + 1, "has a full column")
                                        winning_board = p
                                        win_list.append(p)
                                        # print("Item added to win_list:\n", win_list)
                                        # print("win_list length is:", len(win_list))
                                        # print(np_all_positions)

                                        if len(win_list) == allboards_length:
                                            # print("win_list length contains all boards and is ", len(win_list))
                                            return ()

 
check_for_match()



#FINAL CALCULATIONS:

# Now get last number called and multiply by all non-called numbers in winning board:
print("\nFinal called_number:", called_number)

# Get all the non-called numbers in the winning board and add them up:
print("Last winning_board:", winning_board + 1, "(Index:", winning_board, ")")

not_called_values = []

# Loop through rows and elements of the winning board
for (b, row) in enumerate(np_all_positions[winning_board]):

    for (c, element) in enumerate(row[0: None]):

        if element == 0:
            not_called_values.append(allboards[winning_board][b][c])

# Find final score:
print("Sum not called values:", sum(not_called_values))

final_score = sum(not_called_values) * called_number
print("Final Score Is:", final_score)
