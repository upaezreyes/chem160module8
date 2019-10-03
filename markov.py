import numpy as np
from numpy.linalg import matrix_power

P = np.matrix([[0.25, 0.40], [0.75, 0.60]]) # creates matrix P
print(P)

N = np.matrix([[50],[50]])  # creates matrix N
print(N)   # 50 students sleeping and 50 students studying

N = P*N   # multiplying matrix P times matrix N (after 1 hour)
print(N)  # prints out students sleeping and studying after 1 hour

P10 = matrix_power(P,10)  # after 10 hours
N = P10*N
print(N)  # prints out students sleeping and studying after 10 hours

N = P10*N  # another 10 hours
print(N)

