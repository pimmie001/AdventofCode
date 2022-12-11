import re
from copy import deepcopy


with open('11.txt') as fh:
    input = fh.read().split('\n\n')
n = len(input)


items = {}
operations = {}
tests = {}
throw = {}

# setup
for m in range(n):
    instructions = input[m].split('\n')

    items[m] = [int(x) for x in re.findall('[0-9]+', instructions[1])]

    operator, num = re.findall('old (.*)', instructions[2])[0].split(' ')
    if num == 'old':
        operations[m] = ['sq', None]
    else:
        operations[m] = [operator, int(num)]

    tests[m] = int(re.findall('[0-9]+', instructions[3])[0])

    throw[m] = [int(re.findall('[0-9]+', instructions[4])[0]), int(re.findall('[0-9]+', instructions[5])[0])]

items_copy = deepcopy(items)


def change_worry(worry, operation):
    if operation[0] == 'sq':
        return worry**2
    elif operation[0] == '+':
        return worry + operation[1]
    elif operation[0] == '*':
        return worry * operation[1]


inspected = [0]*n
for round in range(20):
    for m in range(n):
        for worry in items[m]:
            inspected[m] += 1
            worry = change_worry(worry, operations[m])
            worry //= 3
            if worry % tests[m] == 0:
                nextmonk = throw[m][0]
            else:
                nextmonk = throw[m][1]
            items[nextmonk].append(worry)
        items[m] = []

inspected.sort()
print(inspected[-1] * inspected[-2]) # part 1: 118674


### part 2:
N = 1
for x in tests.values():
    N *= x

items = items_copy
inspected = [0]*n
for round in range(10000):
    for m in range(n):
        for worry in items[m]:
            inspected[m] += 1
            worry = change_worry(worry, operations[m])
            worry %= N
            if worry % tests[m] == 0:
                nextmonk = throw[m][0]
            else:
                nextmonk = throw[m][1]
            items[nextmonk].append(worry)
        items[m] = []

inspected.sort()
print(inspected[-1] * inspected[-2]) # 32333418600
