with open("8.txt") as fh:
    content = fh.read().split("\n")

strcount = 0
memcount = 0

for line in content:
    strcount += len(line)
    memcount += len(eval(line))

print("Answer part 1: ",strcount-memcount)


### Part 2
count = 0
for line in content:
    newline = '"'
    for character in line:
        if character == '"':
            newline += r'\"'
        elif character == "\\":
            newline += r'\\'
        else:
            newline += character
    newline += '"'

    count += len(newline) - len(line)

print("Answer part 2: ",count)