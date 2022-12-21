# 85. Maximal Rectangle

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

lenth=len(matrix)
max_num=matrix[0][0]

for i in range(lenth):
    