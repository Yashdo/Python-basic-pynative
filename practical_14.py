# Longest Common Prefix


strs = ["flower","flow","flight"]

i = len(strs[0])
for j in range( len(strs)):
    i = min(i, len(strs[j]))
    while i > 0 and strs[0][0:i] != strs[j][0:i]:
        i -= 1
print (strs[0][0:i])
    