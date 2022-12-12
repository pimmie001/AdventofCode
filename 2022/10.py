with open('10.txt') as fh:
    instructions = fh.read().split('\n')


cycles = [20, 60, 100, 140, 180, 220]
Values = []

X = 1
n = None
i = 0
cycle = 1
while cycle <= cycles[-1]:
    if n:
        X += n
        cycle += 1

        if cycle in cycles:
            Values.append(X*cycle)

    instruction = instructions[i]
    if 'addx' in instruction:
        n = int(instruction.split(' ')[1])
    else: 
        n = None

    i += 1
    cycle += 1

    if cycle in cycles:
        Values.append(X*cycle)

print(sum(Values)) # part 1: 15220


### part 2:
X = 1
n = None
i = 0
cycle = 0
while cycle < 6*40:
    if cycle % 40 == 0:
        print()
    if abs(cycle % 40 - X) <= 1:
        print('#', end='')
    else:
        print('.', end='')

    if n:
        X += n
        cycle += 1

        if cycle % 40 == 0:
            print()
        if abs(cycle % 40 - X) <= 1:
            print('#', end='')
        else:
            print('.', end='')

    instruction = instructions[i]
    if 'addx' in instruction:
        n = int(instruction.split(' ')[1])
    else: 
        n = None

    i += 1
    cycle += 1

# part 2: RFZEKBFA
