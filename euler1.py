import numpy as np

N = 1000    # max number
m3 = np.arange(0,N,3)    # all multiples of 3 from zero to N=1000
m5 = np.arange(0,N,5)    # all multiples of 5 from zero to N=1000

m35 = np.concatenate([m3,m5])  # list that contains all the multiples of 3 and 5
m35u = np.unique(m35)   # sum all of the multiple numbers of 3 and 5
                        # but removes of the doubles numbers

print("sum of 3 and 5 multiples below %d is %d"%(N,m35u.sum()))