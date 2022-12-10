with open('10.txt') as fh:
    instructions = fh.read().split('\n')


cycles = [20, 60, 100, 140, 180, 220]
Values = []

X = 1
n = None
i = 0
cycle = 1
while cycle <= cycles[-1]:
    if cycle in cycles:
        Values.append(X*cycle)

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

    i = (i+1)%len(instructions)
    cycle += 1

print(sum(Values)) # part 1: 15220

