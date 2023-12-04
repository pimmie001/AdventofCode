import re

with open('4.txt') as fh:
    content = fh.read().split('\n')


def points(winning, own):
    count = 0
    for card in own:
        if card in winning:
            count += 1

    if count == 0:
        return 0
    return 2 ** (count - 1)


total = 0
for line in content:
    line = line.split(':')[1]
    winning, own = line.split('|')
    winning = re.findall(r'\d+', winning)
    own = re.findall(r'\d+', own)

    total += points(winning, own)

print(total) # part 1: 21919

