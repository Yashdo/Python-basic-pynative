# 329. Longest Increasing Path in a Matrix

matrix = [[9,9,4],
          [6,6,8],
          [2,1,1]]

lenth=len(matrix)
next=None

for row in range(lenth):
    for col in range(lenth):
        