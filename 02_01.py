
thefilepath = "02_01_Data.txt"

with open(thefilepath) as f:
    file_list = f.readlines()

#file_list = ['forward 5\n', 'down 5\n', 'forward 8\n', 'up 3\n', 'down 8\n', 'forward 2']

#print(file_list)

forward_str = "forward"
forward_int = 0
down_str = "down"
down_int = 0
up_str = "up"
up_int = 0

#Identify all the lines with the word 'forward' contained.


#seach for lines containing 'forward' string
#then extract the integer (2nd last element of each line [/n character is last!]
#then add result to counter variable "forwrard_int".


for line in file_list:
    if forward_str in line:
        result = int(line[-2:])
        forward_int = forward_int + result
        #print(result, forward_int)
        result = 0
    else:
        #print ("does not have 'forward' in line")
        #probably don't need this but just in case.....
        result = 0


#Now do the exact same for 'Down'

for line in file_list:
    if down_str in line:
        result = int(line[-2:])
        down_int = down_int + result
        #print(result, down_int)
        result = 0
    else:
        #print ("does not have 'down' in line")
        result = 0

#And the same for 'Up'

for line in file_list:
    if up_str in line:
        result = int(line[-2:])
        up_int = up_int + result
        #print(result, up_int)
        result = 0
    else:
        #print ("does not have 'up' in line")
        result = 0
        
        


#Calculate finale depth:

depth = down_int - up_int


#Calculate final 'multiplied position':
multiplied_pos = forward_int * depth


#Print Final Results 
print("Forward Line Integer Count", forward_int)
print("DOwn Line Integer Count", down_int)
print("Up Line Integer Count", up_int)
print("Depth Is:", depth)
print("Final Multiplied Position:", multiplied_pos)




