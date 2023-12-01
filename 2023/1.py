with open('1.txt') as fh:
    content = fh.read().split('\n')

total = 0
for line in content:
    found_first = False
    last = None
    for letter in line:
        if letter.isnumeric():
            if found_first:
                last = letter
            else:
                first = letter
                found_first = True

    if last:
        total += int(first+last)
    else:
        total += int(first+first)

print(total) # part 1: 55447