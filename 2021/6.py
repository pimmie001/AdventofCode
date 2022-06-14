from typing import Counter
import numpy as np
import re

with open('6.txt') as f:
    content = f.read()
    input = np.array(re.split(',|\n', content), dtype = int)

def nextday(currentday):
    newday = {}
    currentday = currentday.copy()
    # change counter by -1 for 1 trough 7
    for i in range(8):
        newday[i] = currentday.get(i+1, 0) # default value 0  

    nozero = currentday.get(0, 0) # number of zeros in current day
    newday[6] += nozero # reset timer to 6 for new fish (add to total)
    newday[8] = nozero # the extra fish start with counter 8

    return newday


def moredays(A, n):
    # does the above n times
    A = A.copy()
    for it in range(n):
        A = nextday(A)
    return A


for n in [80, 256]:
    beginday = Counter(input)
    endday = moredays(beginday, n) # do the thing n times

    print(sum(endday.values())) # print the sum of values in dictionary 

# part 1: 390923
# part 2: 1749945484935