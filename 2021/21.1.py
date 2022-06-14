# # example
# start1 = 4
# start2 = 8

# own input
start1 = 4
start2 = 6


def newpos(curpos, steps):
    steps %= 10
    new = curpos + steps
    return new if new <= 10 else new - 10

def nextdie(prevdie = 0):
    return 1 if prevdie == 100 else prevdie + 1

score1 = 0
score2 = 0
player1turn = 1
pos1 = start1
pos2 = start2
diecount = 0
prevdie = 0
while score1 < 1000 and score2 < 1000:
    steps = 0
    for i in range(3):
        die = nextdie(prevdie)
        prevdie = die
        steps += die
        diecount += 1

    if player1turn:
        pos1 = newpos(pos1, steps)
        score1 += pos1
    else:
        pos2 = newpos(pos2, steps)
        score2 += pos2

    player1turn = 1 - player1turn

print(diecount * min(score1, score2)) # 888735
