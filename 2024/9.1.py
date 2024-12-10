from collections import deque

with open("9.txt") as fh:
    disk = fh.read()


## 1. setup: make layout
blocks = []
empty_indices = deque([])
j = 0

for i, x in enumerate(disk):
    x = int(x)

    if i % 2 == 0:
        for _ in range(x):
            blocks.append(i//2)
            j += 1

    else:
        for _ in range(x):
            blocks.append(None)
            empty_indices.append(j)
            j += 1



## 2. Move stuff
def print_situation(blocks):
    for x in blocks:
        if x is None:
            print(".", end="")
        else:
            print(x, end="")
    print()
    return


while empty_indices:
    # print_situation(blocks)
    # print(empty_indices)
    # print()

    blocks[empty_indices.popleft()] = blocks.pop()

    while blocks[-1] is None:
        blocks.pop()
        empty_indices.pop()


print(sum([x*y for x,y in enumerate(blocks)])) # part 1: 6415184586041

