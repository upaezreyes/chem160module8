import math, time
t = time.process_time()
max= 100000000

sum = 0.0   # to keep track of the sum of the first max+1 numbers

for i in range(1,max+1):  # loop from 1 to max+1
    sum += math.sqrt(i)  #  take the sqrt of each number and add them together

elapsed_time = time.process_time() - t

print("Sum of sqrt of first ", max, "Numbers=", sum, "time=", elapsed_time)