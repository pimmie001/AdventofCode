import re

with open('13.txt') as fh:
    content = fh.read().split('\n\n')

machines = []
for text in content:
    numbers = re.findall(r'\d+', text)
    numbers = list(map(int, numbers))
    machines.append(numbers)


def fewest_tokens(machine, x=0, y=0, current_spend=0, memo={}):
    """
    Function that takes as input machine (tuple of length 6 describing what buttons do an how to win), 
    and the nummer of currently spend tokens (current_spend). x and y are current x and y values. 
    Returns minimum number of tokens required to win, and infinity if not possible.
    Not sure if memo works as supposed to. 
    """

    ### Base cases
    if x > machine[4] or y > machine[5]:
        return float('inf')

    if x == machine[4] and y == machine[5]:
        return current_spend

    if (x,y) in memo:
        return memo[(x,y)]


    ### Return minimum of both moves
    resultA = fewest_tokens(machine, x+machine[0], y+machine[1], current_spend+3, memo) # press A
    resultB = fewest_tokens(machine, x+machine[2], y+machine[3], current_spend+1, memo) # press B
    memo[(x,y)] = min(resultA, resultB)
    return min(resultA, resultB)


total = 0
for machine in machines:
    memo = {}
    result = fewest_tokens(machine, memo={})

    if result < float('inf'):
        total += result

print(total) # part 1: 27105
