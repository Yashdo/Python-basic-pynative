# Write a Python program to get the Fibonacci series

series=10
n1, n2 = 0, 1
for i in range(1,series+1):

    # fibonacci = (i-1)+(i-2)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

