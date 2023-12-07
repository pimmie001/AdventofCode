import numpy as np
from collections import Counter


with open('7.txt') as fh:
    content = fh.read().split('\n')

hands = []
bids = []
for x in content:
    y = x.split(' ')
    hands.append(y[0])
    bids.append(int(y[1]))


def get_scores(hand):
    """given a hand, return scores this hand (type, card1, card2, ..., card5)"""

    ## count cards
    letter_counts = Counter(hand)
    counts = sorted(list(letter_counts.values()), reverse=True)


    ## determine type (5 of a kind, full house etc. )
    if counts[0] == 5:
        type = 6
    elif counts[0] == 4:
        type = 5
    elif counts[0] == 3 and counts[1] == 2:
        type = 4
    elif counts[0] == 3:
        type = 3
    elif counts[0] == 2 and counts[1] == 2:
        type = 2
    elif counts[0] == 2:
        type = 1
    else: 
        type = 0

    ## find strenght of cards
    strengths = [] # strenght of cards in hand
    for card in hand:
        if card.isnumeric():
            strengths.append(int(card))
        elif card == 'T':
            strengths.append(10)
        elif card == 'J':
            strengths.append(11)
        elif card == 'Q':
            strengths.append(12)
        elif card == 'K':
            strengths.append(13)
        elif card == 'A':
            strengths.append(14)

    return (type,) + tuple(strengths)


def abeforeb(a, b):
    # returns wether a <= b where a and b are tuples

    for i in range(len(a)):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False
    return True

def check_sorted(scores, j=0):
    # checks if scores is sorted, if so returns True, else returns first index that is higher than its neighbor
    # only checks indices j or larger

    for i in range(j, len(scores) - 1):
        a = scores[i]
        b = scores[i+1]

        if not abeforeb(a, b):
            return False, i

    return True, None


scores = []
for i in range(len(hands)):
    hand = hands[i]
    scores.append(get_scores(hand))


I = np.arange(len(scores))
i = 0
hands_copy = hands.copy()
while True:
    is_sorted, i = check_sorted(scores, max(0, i-1))
    if is_sorted:
        break

    scores[i], scores[i+1] = scores[i+1], scores[i]
    I[i], I[i+1] = I[i+1], I[i]


total = 0
for i in range(len(bids)):
    total += bids[I[i]] * (i+1)
print(total) # part 1: 252052080  
