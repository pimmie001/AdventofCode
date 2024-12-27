with open('19.txt') as fh:
    available, targets = fh.read().split('\n\n')
    available = available.split(', ')
    targets = targets.split('\n')


def count_options(current, available=available, memo={}):
    ## base cases
    if current == "":
        return 1

    if current in memo:
        return memo[current]

    ## recursive case
    options = []
    for string in available:
        if current.endswith(string):
            options.append(current[:-len(string)])

    total = 0
    for option in options:
        total += count_options(option, available=available, memo=memo)
    memo[current] = total
    return total


grand_total = 0
for target in targets:
    grand_total += count_options(target)
print(grand_total) # part 2: 635018909726691