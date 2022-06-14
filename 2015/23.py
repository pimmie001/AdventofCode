with open("23.txt") as fh:
    instructions = fh.read().split("\n")


# values = {"a":0, "b":0}     # Part 1
values = {"a":1, "b":0}     # Part 2
i = 0
while i >=0 and i < len(instructions):
    instruction = instructions[i]
    if "inc" in instruction:
        target = instruction.split()[1]
        values[target] += 1
        i += 1
    elif "tpl" in instruction:
        target = instruction.split()[1]
        values[target] *= 3
        i += 1
    elif "hlf" in instruction:
        target = instruction.split()[1]
        values[target] //= 2
        i += 1
    elif "jmp" in instruction:
        amount = int(instruction.split()[1])
        i += amount
    elif "jie" in instruction:
        instruction = instruction.replace("jie","").replace(" ","").split(",")
        target = instruction[0]
        amount = int(instruction[1])
        if values[target] % 2 == 0:
            i += amount
        else:
            i += 1
    elif "jio" in instruction:
        instruction = instruction.replace("jio","").replace(" ","").split(",")
        target = instruction[0]
        amount = int(instruction[1])
        if values[target] == 1:
            i += amount
        else: 
            i += 1

print(values)