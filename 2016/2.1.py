with open("2.txt") as fh:
    instructions = fh.read().split("\n")

position = 5
password = ""

for instruction in instructions: 
    for x in instruction:
        if x == "U" and position > 3:
            position -= 3
        elif x == "D" and position < 7:
            position += 3
        elif x == "L" and position % 3 != 1:
            position -= 1
        elif x == "R" and position % 3 != 0:
            position += 1

    password += str(position)

print(password)
