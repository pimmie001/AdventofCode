with open('8.txt') as fh:
    instructions, lines = fh.read().split('\n\n')


graph = {}

lines = lines.split('\n')
for line in lines:
    start, dest = line.split(' = ')
    left, right = dest[1:-1].split(', ')
    graph[start] = (left, right)


current = 'AAA'
i = 0
while current != 'ZZZ':
    direction = instructions[i%len(instructions)]
    if direction == 'L':
        current = graph[current][0]
    else:
        current = graph[current][1]
    i += 1
print(i) # part 1: 17287
