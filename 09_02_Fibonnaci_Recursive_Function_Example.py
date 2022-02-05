# Python program to display the fibonaci sequence

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is within given range

if nterms <= 0:
    print("please enter a positive integer for 'nterms' in code")
else:
    print("Fibonacci Sequence:")
    # Note: range starts at 0 and stops BEFORE final number (doesn't include it)
    for i in range(nterms):
        print(recur_fibo(i))
