# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

s1 = "America"
s2 = "Japan"

# get A & J 
res = s1[0] + s2[0]
# get lenth of s1
l = len(s1)
# get R
res = res +s1[l-4]
# get pan
res = res + s2[2:]

print(res)


