user_input=int(input("Enter your number : "))

for i in range(1,user_input+1):

    for j  in range(i-1,user_input-1):
        print(" ",end=' ')

    for j in range(i,i*2):
        pascal=(i+j-1)*(j-i*i)
        print(pascal,end=' ')

    print("\n")