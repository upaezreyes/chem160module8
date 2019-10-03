import numpy as np
def neighbors(arr,x,y,n):
    arr = np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]

a = np.arange(0,100).reshape(10,10)  # creates an 10x10 array
print(a)
print(neighbors(a,0,0,3))  # creates a 3x3 array with values around position 0o
print(neighbors(a,0,0,5))  # creates a 5x5 array with values around position 0