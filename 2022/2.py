with open('2.txt') as fh:
    content = fh.read().split('\n')

win = set((('A','Y'), ('B','Z'), ('C','X')))
draw = set((('A','X'), ('B','Y'), ('C','Z')))

score = 0
for play in content:
    # score = 0
    opponent, myself = play.split(' ')
    
    if myself == 'X':
        score += 1
    elif myself == 'Y':
        score += 2
    else: 
        score += 3

    if (opponent, myself) in win:
        score += 6
    elif (opponent, myself) in draw:
        score += 3


print(score) # part 1: 14069

A = ['A', 'B', 'C']
B = ['X', 'Y', 'Z']


score2 = 0
for play in content:
    opponent, strat = play.split(' ')
    ind = A.index(opponent)

    if strat == 'X':
        myind = (ind-1)%3
    elif strat == 'Y':
        myind = ind
        score2 += 3
    else:
        myind = (ind+1)%3
        score2 += 6

    myself = B[myind]
    if myself == 'X':
        score2 += 1
    elif myself == 'Y':
        score2 += 2
    else: 
        score2 += 3

print(score2) # part 2: 12411
