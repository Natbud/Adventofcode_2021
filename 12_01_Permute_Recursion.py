
def rec_permute(sofar, rest):
    if rest == "":
        print(sofar, exit())
    else:
        for i in range(len(rest)):
            next = sofar + rest[i]
            remaining = rest[0:i-1]
            rec_permute(next, remaining)


#driver code:
rest = "abcd"
#input("please enter string:")
rec_permute("", rest)
