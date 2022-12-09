# Longest Common Prefix


strs = ["flower","flow","flight"]
"""
:type strs: List[str]
:rtype: str
"""
# if len(strs) == 0:
#     print(" ")
# if len(strs) == 1:
#     print(strs[0])
i = len(strs[0])
for j in range(1, len(strs)):
    i = min(i, len(strs[j]))
    while i > 0 and strs[0][0:i] != strs[j][0:i]:
        i -= 1
    if i == 0:
        print("")
print (strs[0][0:i])
    
    


"""Secound method"""
    
words =["flower","flow","flight"]
   
print("Duplicate words in a given string : ");  
for i in range(0, len(words)):  
    count = 1;  
    for j in range(i+1, len(words)):  
        if(words[i] == (words[j])):  
            count = count + 1  
            #Set words[j] to 0 to avoid printing visited word  
            words[j] = "0"  
              
    #Displays the duplicate word if count is greater than 1  
    if(count > 1 and words[i] != "0"):  
        print(words[i])
