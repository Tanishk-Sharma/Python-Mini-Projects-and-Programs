######################################################################
# Write a program to print the Fibonacci series upto nth element     #
# NOTE: user recursive function.                                     #
######################################################################

n = int(input("Enter n: "))

def fibo(x):
    if x==0 or x==1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


for num in range(n):
	print(str(fibo(num)) + ",", end="")
