from dokusan import generators
import numpy as np

arr=np.array(list(str(generators.random_sudoku(avg_rank=150))))
print(arr.reshape(9,9))

# suduku = []
# # user_input=int(input("Enter your value : "))
# for i in range(9):
#     row = list(input("Enter Element of row {} without any spaces".format(i+1)))
#     row = [int(i) for i in row]
# print(np.matrix(suduku))


# def possible(y, x, n):
#     global suduku
#     for i in range(9):
#         if suduku[y][i] == n:
#             return False
#     for i in range(9):
#         if suduku[i][x] == n:
#             return False
#     box_y = (y//3)*3
#     box_x = (y//3)*3
#     for i in range(3):
#         for j in range(3):
#             if suduku[box_y+i][box_x+j] == n:
#                 return False
#     return True


# def solve():
#     for y in range(3):
#         for x in range(3):
#             if suduku[y][x] == 0:
#                 for n in range(1, 10):
#                     if possible(y, x, n):
#                         suduku[y][x] = n
#                         solve()
#                         suduku[y][x] = 0
#                 return
#     print(np.matrix(suduku))
#     print("More??")


# solve()
