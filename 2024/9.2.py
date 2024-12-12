with open("9.txt") as fh:
    disk = fh.read()


## 1. setup: make layout
blocks = []
empty_indices = []
id_lenghts = []
first_index_of_id= {}
j = 0

for i, x in enumerate(disk):
    x = int(x)

    if i % 2 == 0:
        first_index_of_id[i//2] = j
        id_lenghts.append((i//2, x)) # id, length
        for _ in range(x):
            blocks.append(i//2)
            j += 1

    else:
        empty_indices.append((j, x)) # position, number of spaces
        for _ in range(x):
            blocks.append(None)
            j += 1



## 2. Move stuff

while id_lenghts:
    id, length = id_lenghts.pop() # most right id and its length

    for index_empty_indices, (i, num) in enumerate(empty_indices):
        if num >= length and i < first_index_of_id[id]: # there is space and empty space is left of index of id

            ## move blocks
            for j in range(length):
                blocks[i+j], blocks[first_index_of_id[id]+j] = blocks[first_index_of_id[id]+j], blocks[i+j]

            ## update empty indices
            empty_indices.pop(index_empty_indices)
            if num > length:
                empty_indices.append((i+length, num-length)) # new position, remaining empty spaces
                empty_indices = sorted(empty_indices, key = lambda x: x[0])

            break



## 3. calculate checksum
total = 0
for x,y in enumerate(blocks):
    if y:
        total += x*y
print(total) # part 2: 6436819084274 
