# Write a program to create a new string made of an input string’s first, middle, and last character.

a = "james"

ans=a[0]

l=len(a) # l = 5

secoun_Value = int(l/2) #secoun_Value is 3
# get secound value
ans= ans + a[secoun_Value]
# get last value
ans= ans + a[l-1]

print(ans)




