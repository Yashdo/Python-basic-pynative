# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

mi = int(len(s1)/2)

res=s1[:2:]

res=res+s2+s1[2:]
print(res)

