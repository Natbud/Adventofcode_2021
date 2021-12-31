
#thefilepath = "02_02_Test_Data.txt"

#with open(thefilepath) as f:
#     file_list = f.readlines()

file_list = ['forward 5\n', 'down 5\n', 'forward 8\n', 'up 3\n', 'down 8\n', 'forward 2']
print(file_list)

forward_str = "forward"
forward_int = 0
down_str = "down"
down_int = 0
up_str = "up"
up_int = 0
aim_int = 0
depth = 0

#Identify all the lines with the word 'forward' contained.

#seach for lines containing 'forward' string
#then extract the integer (2nd last element of each line [/n character is last!]
#then add result to counter variable "forwrard_int".

for line in file_list:
    if forward_str in line:
        #Get 2nd last object in the line (the number as
        #there is a retunrn character at end:
        result = int(line[-2:])
        forward_int = forward_int + result
        depth = depth + (aim_int * result)
        print("x:", result, "fd int:", forward_int, "depth:", depth)
               
    if down_str in line:
        result = int(line[-2:])
        aim_int = aim_int + result
              
    if up_str in line:
        result = int(line[-2:])
        aim_int = aim_int - result 

#Calculate final multiplied position:
multiplied_pos = forward_int * depth

#Print Final Results 
print("Forward Line Integer Count", forward_int)
print("Depth Is:", depth)
print("Final Multiplied Position:", multiplied_pos)




