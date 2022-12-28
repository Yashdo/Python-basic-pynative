# 329. Longest Increasing Path in a Matrix

matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]

row_len, col_len = len(matrix), len(matrix[0])
paths = [[0 for _ in range(col_len)] for _ in range(row_len)]
print(paths)

for row in range(row_len):
    for col in range(col_len):

        if [row][col] != 1:
  
            if matrix[row][col] > matrix[row][col+1]: 
                paths[row][col] += 1
                # print(paths[row][col])
     
            if matrix[row][col] > matrix[row+1][col]:
                paths[row][col] += 1
                # print(paths[row][col])

            if matrix[row][col] > matrix[row][col+1]:
                paths[row][col] += 1
                # print(paths[row][col])

            if matrix[row][col] > matrix[row-1][col]:
                paths[row][col] += 1
                print(paths[row][col])











































# def getpathfrom(i, j, prevval):

    # if (i < 0) or (j < 0) or (i == m) or (i == n) or (matrix[i][j] <= prevval):
        # return 0

    # if (paths[i][j] != 0):
        # return paths[i][j]

    # paths[i][j] = 1 + max([getpathfrom(i+x, j+y, matrix[i][j])
                        #   for x, y in dirs])

    # return paths[i][j]


# longestpath = 0
# m, n = len(matrix), len(matrix[0])
# paths = [[0 for _ in range(n)] for _ in range(m)]
# dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# for i in range(m):
    # for j in range(n):

        # currentpath = getpathfrom(i, j, -1)
        # longestpath = max(longestpath, currentpath)
# print(longestpath)