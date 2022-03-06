import nltk
from nltk.corpus import words
#nltk.download('words')

#d = enchant.Dict()


anagrams = []

def rec_permute(sofar, rest):
    # This checks if a string has been generated from all the characters:
    # If so, prints the current permutation/anagram:
    if rest == "":
        # print(sofar)
        anagrams.append(sofar)
    else:
        #takes the lengths of the initial character string 'rest'
        for i in range(len(rest)):
            # adds a character from 'rest' to the new 'sofar' (whic his now called 'next')
            next = sofar + rest[i]
            # sets remaiining (the new 'rest' to everything before and after 'i'
            # in rest.  so removes 'i' from 'rest'
            remaining = rest[:i] + rest[i+1:]
            rec_permute(next, remaining)

#driver code:
rest = "meats"
rec_permute("", rest)

#PRINT RESULTS:
print("checking anagrams with dictionary.....")
count = 1
for i in set(anagrams):
    # check if anagram is in dictionary
    if i in words.words():
        print(count, i)
    count +=1
print("number of anagrams including duplicates:", len(anagrams))
print("number of anagrams without duplicates:", len(set(anagrams)))
