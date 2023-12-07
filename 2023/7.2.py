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


#### functions ####

def extend_options(options, i):
    """at place i (where Joker should be) replace with all possible options"""

    replacements = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    new_options = []
    for option in options:
        for card in replacements:
            new_hand = option[:i] + card + option[i+1:]
            new_options.append(new_hand)

    return new_options


def get_type(hand):
    """given a hand, get type"""

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

    return type


def get_best_type(hand):
    """given a hand, get best type (for any value of Joker)"""

    options = [hand]
    while 'J' in options[0]:
        i = options[0].index('J')
        options = extend_options(options, i)

    type = 0
    for hand in options:
        type = max(type, get_type(hand))

    return type


def get_scores(hand):
    """given a hand, return scores this hand"""

    type = get_best_type(hand) 

    ## find strenght of cards
    strengths = [] # strenght of cards in hand
    for card in hand:
        if card.isnumeric():
            strengths.append(int(card))
        elif card == 'T':
            strengths.append(10)
        elif card == 'J':
            strengths.append(1) # joker now the lowest
        elif card == 'Q':
            strengths.append(12)
        elif card == 'K':
            strengths.append(13)
        elif card == 'A':
            strengths.append(14)

    n = 14 # upperbound on values
    score = n**len(strengths) * type
    for i in range(len(strengths)):
        score += n**(len(strengths)-1-i) * strengths[i]
    return score


## get scores
scores = []
for i in range(len(hands)):
    hand = hands[i]
    scores.append(get_scores(hand))

I = np.argsort(scores)

total = 0
for i in range(len(bids)):
    total += bids[I[i]] * (i+1)
print(total) # part 2: 252898370  
