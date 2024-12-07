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
for x in page_numbers:
    seq = [int(y) for y in x.split(',')]
    total += seq[len(seq)//2] * validate_sequence(seq)

print(total) # part 1: 5991 