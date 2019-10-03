import numpy as np
from numpy.linalg import inv

A = np.matrix([[1,2,3],[2,4,5],[3,5,6]])  # creates a matrix
print("matrix A:",A)

B = inv(A)  # inverse of matrix A
print("matrix B:",B)

C = B*A   # multipy matrix B by matrix B
print("matrix C:",C)