import numpy as np
import re

def checkifbingo(Y): # for part 1
    m, n = np.shape(Y)[:2]
    for card in range(m):
        rowsum = np.sum(Y[card,:,:], axis = 1)
        colsum = np.sum(Y[card,:,:], axis = 0)
        if np.any(rowsum == n) or np.any(colsum == n): 
            return (True, card)
    return [False]

with open ('4.txt') as fh:
    input = fh.read().split('\n\n')

numbers = np.array(input[0].split(','), dtype = int)
input = input[1:]

m = len(input) # number of bingo cards
n = len(input[0].split('\n')) # size of bingo card (assuming square)

X = []
for i in range(m):
    a = re.split('\n| ' ,input[i])
    for x in a:
        if x != '': X.append(x)
X = np.array(X, dtype = int).reshape((m,n,n))
# X is 3 dimensional array containing all bingo cards
Y = np.zeros(shape = np.shape(X), dtype = bool)
# Y is 3 dimensianal array that will keep track of the numbers that have been drawn 
Z = np.copy(Y) # same but for part 2


### part 1
for number in numbers:
    indices = np.where(X == number)
    Y[indices] = True
    if checkifbingo(Y)[0]: break
winning_card = checkifbingo(Y)[1]

x = X[winning_card]
unmarked_sum = np.sum(x[np.where(Y[winning_card] == False)])
print(unmarked_sum * number) # final answer part 1: 10680


### part 2
def howmanybingo(Y):
    m, n = np.shape(Y)[:2]
    count = 0
    for card in range(m):
        rowsum = np.sum(Y[card,:,:], axis = 1)
        colsum = np.sum(Y[card,:,:], axis = 0)
        if np.any(rowsum == n) or np.any(colsum == n): 
            count += 1
    return count

def whichcard(Y):
    # returns which card does not yet have bingo
    m, n = np.shape(Y)[:2]
    for card in range(m):
        rowsum = np.sum(Y[card,:,:], axis = 1)
        colsum = np.sum(Y[card,:,:], axis = 0)
        if not( np.any(rowsum == n) or np.any(colsum == n)): 
            return card
    return None


for number in numbers:
    wincount = howmanybingo(Z)
    if wincount == m-1: lastcard = whichcard(Z) # find last card

    indices = np.where(X == number)
    Z[indices] = True

    if howmanybingo(Z) == m: break # break once last card has bingo

x = X[lastcard]
unmarked_sum = np.sum(x[np.where(Z[lastcard] == False)])
print(unmarked_sum * number) # final answer part 2: 31892