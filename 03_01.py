thefilepath = "03_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()

#Input TEST Data:
#file_list = ['00100\n', '11110\n', '10110\n', '10111\n', '10101\n', '01111\n', '00111\n', '11100\n', '10000\n', '11001\n', '00010\n', '01010']

#print(file_list)

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
gamma = []
epsilon = []

for line in file_list:
    result = int(line[0])
    Pos1.append(result)
    result = int(line[1])
    Pos2.append(result)
    result = int(line[2])
    Pos3.append(result)
    result = int(line[3])
    Pos4.append(result)
    result = int(line[4])
    Pos5.append(result)
    result = int(line[5])
    Pos6.append(result)
    result = int(line[6])
    Pos7.append(result)
    result = int(line[7])
    Pos8.append(result)
    result = int(line[8])
    Pos9.append(result)
    result = int(line[9])
    Pos10.append(result)
    result = int(line[10])
    Pos11.append(result)
    result = int(line[11])
    Pos12.append(result)
    # print("LN 1 CHR 1:", result)


# Now Find Most Frequent Value In THe List GOT TO BE A MORE EFFICIENT
# WAY TO DO/LOOP THIS!:
def most_frequent1(Pos1):
    return max(set(Pos1), key=Pos1.count)
def most_frequent2(Pos2):
    return max(set(Pos2), key=Pos2.count)
def most_frequent3(Pos3):
    return max(set(Pos3), key=Pos3.count)
def most_frequent4(Pos4):
    return max(set(Pos4), key=Pos4.count)
def most_frequent5(Pos5):
    return max(set(Pos5), key=Pos5.count)
def most_frequent6(Pos6):
    return max(set(Pos6), key=Pos6.count)
def most_frequent7(Pos7):
    return max(set(Pos7), key=Pos7.count)
def most_frequent8(Pos8):
    return max(set(Pos8), key=Pos8.count)
def most_frequent9(Pos9):
    return max(set(Pos9), key=Pos9.count)
def most_frequent10(Pos10):
    return max(set(Pos10), key=Pos10.count)
def most_frequent11(Pos11):
    return max(set(Pos11), key=Pos11.count)
def most_frequent12(Pos12):
    return max(set(Pos12), key=Pos12.count)

gamma.append((most_frequent1(Pos1)))
gamma.append((most_frequent2(Pos2)))
gamma.append((most_frequent3(Pos3)))
gamma.append((most_frequent4(Pos4)))
gamma.append((most_frequent5(Pos5)))
gamma.append((most_frequent6(Pos6)))
gamma.append((most_frequent7(Pos7)))
gamma.append((most_frequent8(Pos8)))
gamma.append((most_frequent9(Pos9)))
gamma.append((most_frequent10(Pos10)))
gamma.append((most_frequent11(Pos11)))
gamma.append((most_frequent12(Pos12)))

# join all elements in gamma list into a single element and int converts
# to decimal:
result_gamma = int("".join(str(x) for x in gamma), 2)

print("Gamma:", result_gamma)


# print("Gammatype:", type(res)) #elements are INT


# NOW Find LEAST common in Pos2 (Epsilon):

def least_frequent1(Pos1):
    return min(set(Pos1), key=Pos1.count)
def least_frequent2(Pos2):
    return min(set(Pos2), key=Pos2.count)
def least_frequent3(Pos3):
    return min(set(Pos3), key=Pos3.count)
def least_frequent4(Pos4):
    return min(set(Pos4), key=Pos4.count)
def least_frequent5(Pos5):
    return min(set(Pos5), key=Pos5.count)
def least_frequent6(Pos6):
    return min(set(Pos6), key=Pos6.count)
def least_frequent7(Pos7):
    return min(set(Pos7), key=Pos7.count)
def least_frequent8(Pos8):
    return min(set(Pos8), key=Pos8.count)
def least_frequent9(Pos9):
    return min(set(Pos9), key=Pos9.count)
def least_frequent10(Pos10):
    return min(set(Pos10), key=Pos10.count)
def least_frequent11(Pos11):
    return min(set(Pos11), key=Pos11.count)
def least_frequent12(Pos12):
    return min(set(Pos12), key=Pos12.count)

epsilon.append((least_frequent1(Pos1)))
epsilon.append((least_frequent2(Pos2)))
epsilon.append((least_frequent3(Pos3)))
epsilon.append((least_frequent4(Pos4)))
epsilon.append((least_frequent5(Pos5)))
epsilon.append((least_frequent6(Pos6)))
epsilon.append((least_frequent7(Pos7)))
epsilon.append((least_frequent8(Pos8)))
epsilon.append((least_frequent9(Pos9)))
epsilon.append((least_frequent10(Pos10)))
epsilon.append((least_frequent11(Pos11)))
epsilon.append((least_frequent12(Pos12)))

#this joins all the individual 1 and 0 (which are currently individual strings of a list) into one value and also
#converts this from str to decimal using the 'int(string ,2)' (Base 2 is binary) function:
result_epsilon = int("".join(str(x) for x in epsilon), 2)

print("Epsilon:", result_epsilon)

# Calculate final power consumption:

print("Power Consuption:", result_gamma * result_epsilon)
