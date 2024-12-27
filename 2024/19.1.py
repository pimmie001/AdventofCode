with open('19.txt') as fh:
    available, targets = fh.read().split('\n\n')
    available = available.split(', ')
    targets = targets.split('\n')


def is_possible(current, target, available=available):
    n = len(current)
    m = len(target)

    ## Base cases
    if n == m:
        return current == target

    if n > m:
        return False

    if current[:min(n,m)] != target[:min(n,m)]:
        return False

    ## Recursive case
    if len(current) >= len(target):
        return current == target

    next_options = [current + option for option in available]
    for new in next_options:
        if is_possible(new, target, available=available):
            return True
    return False


count = 0
for target in targets:
    if is_possible('', target):
        count += 1
print(count) # part 1: 238
