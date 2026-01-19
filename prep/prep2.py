import numpy as np
from functools import reduce
#################################""" VECTORS"

# a = np.array([1,2,3])

# print(a)

# b = np.arange(0,20,2)
# print(b)

# c = np.linspace(1.0,2.0, 5)
# print(c)

# x = c[::2]
# print(x)

# zeros = np.zeros(5)
# print(zeros)

# print(a.size, len(a), a.shape)


# print(np.sum(a))
# print(np.prod(a))
# print(np.max(a))
# print(np.min(a))


#################################""" matrices"

# mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(mat)
# print(mat[0][1])

# mat2 = np.diag(mat)
# print(mat2)
# print(np.transpose(mat))

# A = np.array([[1, 2],
#               [3, 4]])

# B = np.array([[5, 6],
#               [7, 8]])
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])
# print(np.dot(A,B))

# print(np.linalg.inv(A))
# x = np.array([1, 2])
# print(np.linalg.solve(A,x)) # A X = x
# print(np.linalg.det(A))
# print(np.trace(A))

# A = np.array([[1, 2, 3],
#               [3, 4, 6],
#               [5, 10, 7]])
# print("rang")
# print(np.linalg.matrix_rank(A))
# print("col")
# print(np.amax(A,axis=0)) #chaque column
# print("ligne=")
# print(np.amax(A,axis=1)) #chaque ligne

# print("=========")
# print(np.delete(A,0,axis=1)) 


# new_row = np.array([5, 5, 5])
# D = np.insert(A,1,new_row,axis=0)
# print(D)
# print("reshape dim")
# print(D.reshape(3,4))



def rotate_matrix(matrix):
    mat = np.array(matrix)
    diag = np.diag(mat)
    sum = reduce(lambda acc, b : acc+b,diag)
    return sum

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = rotate_matrix(matrix)
print(f"Diagonal sum after rotation: {result}")
matrix = np.transpose(matrix)
print("Rotated matrix:", matrix)
print("=========")
print(np.amax(matrix,axis=1))
# Expected output:
# Diagonal sum after rotation: 15
# Rotated matrix: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]