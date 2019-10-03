import time
import math
import random

trials = int(input("Enter the number of trials: "))

t = time.process_time()

inside = 0
for i in range(trials):   # the number of trials entered
    x = random.random()
    y = random.random()

    if (x*x + y*y) < 1.0:  # if (x*x+y*y) is less than 1, then add 1 to inside
        inside += 1
pi = 4.*inside/trials
et = time.process_time() - t
print("pi est =%9.6f error=%9.6f time=%f"%(pi,pi-math.pi, et))
