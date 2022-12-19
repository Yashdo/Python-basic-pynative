# def wordBreak(self, s, words):
#     ok = [True]
#     for i in range( len(s)+1):
#         ok += any(ok[j] and s[j:i] in words for j in range(i)),
#     return ok[-1]

# ans=wordBreak("leetcode","leet","code")
# print(ans)

# def wordBreak(self, s, wordDict):

s="leetcode"
word=["leet","code"]

n = len(s)
r = [[False for _ in range(n+1)] for _ in range(n)]
for i in range(0, n):

    for j in range(i+1, n+1):

        if i == 0:

            r[i][j] = s[:j] in word
            # print(s[:j], s[:j] in word
            continue

        elif s[i:j] in word:
            
            r[i][j] = r[i-1][i] or r[i-1][j]
            print(r[i-1][i])
            # print("i : ",i)
            # print("j : ",j)
            # print( r[i-1][i] ,"or", r[i-1][j])
            # print("elif : ",s[i:j])

        else:
            r[i][j] = r[i-1][j]
            print(r[i-1][j])

# print(r)
print(r[i][j])
# print (r[n-1][n])
# print(wordBreak("leetcode","leet","code"))