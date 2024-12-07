with open("5.txt") as fh:
    content = fh.read().split('\n\n')

ordering = content[0].split('\n')
page_numbers = content[1].split('\n')


# create array saving the rules
rules = []
for x in ordering:
    a,b = x.split('|')
    rules.append((int(a), int(b)))


# function that valides a sequence
def validate_sequence(sequence, rules=rules):
    index_map = {element: i for i, element in enumerate(sequence)}

    # Check each rule
    for x, y in rules:
        if index_map.get(x, -1) > index_map.get(y, float('inf')):
            return False
    return True


# count correct sequences
total = 0
incorrect_sequences = []
for x in page_numbers:
    seq = [int(y) for y in x.split(',')]

    if validate_sequence(seq):
        total += seq[len(seq)//2]
    else: # for part 2
        incorrect_sequences.append(seq)

print(total) # part 1: 5991 



def find_incorrect(sequence, rules=rules):
    index_map = {element: i for i, element in enumerate(sequence)}

    # Check each rule
    for x, y in rules:
        if index_map.get(x, -1) > index_map.get(y, float('inf')):
            return index_map[x], index_map[y]
    return True


total2 = 0
for seq in incorrect_sequences:
    result = result = find_incorrect(seq)

    while result != True: # simple bubble sort to put in correct order
        i,j = result
        seq[i], seq[j] = seq[j], seq[i]
        result = find_incorrect(seq)

    total2 += seq[len(seq)//2]

print(total2) # part 2: 5479
