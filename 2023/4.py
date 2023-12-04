import re

with open('4.txt') as fh:
    content = fh.read().split('\n')


def points(winning, own):
    # get number of matches
    count = 0
    for card in own:
        if card in winning:
            count += 1
    return count


total = 0 # for part 1
n = len(content) # number of cards
card_copies = {i:1 for i in range(1, n+1)} # for part 2

for i,line in enumerate(content):
    i += 1
    line = line.split(':')[1]
    winning, own = line.split('|')
    winning = re.findall(r'\d+', winning)
    own = re.findall(r'\d+', own)

    count = points(winning, own)
    if count: 
        total += 2 ** (count-1)

    for j in range(i+1, i+1+count):
        card_copies[j] += card_copies[i]


print(total) # part 1: 21919
print(sum(card_copies.values())) # part 2: 9881048
