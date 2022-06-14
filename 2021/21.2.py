import numpy as np
from typing import Counter

def nextpos(curpos, steps):
    new = curpos + steps
    return new if new <= 10 else new - 10


cap = 21 # score needed to be reached

# use some kind of backwards induction 
# suppose both players are at position 20 and it is player 1's turn: player 1 will win in 3 universes
# suppose the scores are 19,20 and pos = 10,10. now p1 wins in 2 universes (throw 2 or 3) and player wins in 3 (because player 2 always wins in next turn in all 3 universes)
# in total there are 2 * 21**2 * 10 ** 2  (= 88200) combinations (players turn x players score x players pos)

A = {} # will contain all this information
B = {} # how many added (0-27). 27 is complete (all universes), every turn 27 universes get created
for p1turn in (1,0):
    for score1 in range(cap):
        for score2 in range(cap):
            for pos1 in range(1,11):
                for pos2 in range(1,11):
                        B[p1turn,score1,score2,pos1,pos2] = 0
                        A[p1turn,score1,score2,pos1,pos2] = np.array([0,0], dtype = np.longlong)

a = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            a.append(i+j+k)
OCC = Counter(a) # {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}, the possibilities of the sum of 3 dices and the number of occurences


while sum(B.values()) < 27 * len(B):
    for p1turn in (1,0):
        for score1 in range(cap):
            for score2 in range(cap):
                for pos1 in range(1,11):
                    for pos2 in range(1,11):

                        if B[p1turn,score1,score2,pos1,pos2] != 27:
                            if p1turn == 1:
                                for roll in OCC:
                                    oc = OCC[roll]
                                    newpos = nextpos(pos1,roll)
                                    if score1 + newpos >= cap:
                                        A[p1turn,score1,score2,pos1,pos2][0] += oc
                                        B[p1turn,score1,score2,pos1,pos2] += oc
                                    elif B[1-p1turn,score1+newpos,score2,newpos,pos2] == 27:
                                        A[p1turn,score1,score2,pos1,pos2] += oc*A[1-p1turn,score1+newpos,score2,newpos,pos2]
                                        B[p1turn,score1,score2,pos1,pos2] += oc

                            else: #p2turn
                                for roll in OCC:
                                    oc = OCC[roll]
                                    newpos = nextpos(pos2,roll)
                                    if score2 + newpos >= cap:
                                        A[p1turn,score1,score2,pos1,pos2][1] += oc
                                        B[p1turn,score1,score2,pos1,pos2] += oc
                                    elif B[1-p1turn,score1,score2+newpos,pos1,newpos]:
                                        A[p1turn,score1,score2,pos1,pos2] += oc*A[1-p1turn,score1,score2+newpos,pos1,newpos]
                                        B[p1turn,score1,score2,pos1,pos2] += oc
                                
                            if B[p1turn,score1,score2,pos1,pos2] != 27:
                                B[p1turn,score1,score2,pos1,pos2] = 0
                                A[p1turn,score1,score2,pos1,pos2] = np.array([0,0], dtype = np.longlong)

# p1 always start and both players start with score 0, p1 and p2 is input
p1 = 4
p2 = 6
print(max(A[1,0,0,p1,p2])) # 647608359455719
