import numpy as np
arr = np.arange(1,25)
print(arr)  # print a 1D array [1,2,...,25]

arr = arr.reshape((3,8))  # reshape to a 2D array,  3x8 array
print(arr)

arr = arr.reshape((2,3,4))  # reshape to a 3D array (2x3x4)
print(arr)

arr = arr.reshape((6,4))  # reshape to a 2D array, 6x4 array
print(arr)

colsum = arr.sum(axis = 0)  # sum of the column on axis 0
print(colsum)
rowsum = arr.sum(axis=1)  # sum of the row on axis 1
print(rowsum)
rowmax = arr.max(axis=1)
print(rowmax)
colmean = arr.mean(axis=0)
print(colmean)