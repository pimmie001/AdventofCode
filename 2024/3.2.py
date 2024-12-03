with open("3.txt") as fh:
    s = fh.read()


A = []
i = 0
look_for_mul = True
do = True

while i < len(s):
    if s[i:i+7] == "don't()":
        do = False
    if s[i:i+4] == "do()":
        do = True

    if look_for_mul:
        if s[i:i+4] == 'mul(':
            a = ''
            i += 4
            look_for_mul = False
        else:
            i += 1

    else:
        char = s[i]

        if char == ')':
            if do:
                A.append(a)
            look_for_mul = True

        elif char.isnumeric() or char == ',':
            a += char

        else:
            look_for_mul = True

        i += 1


total = 0
for a in A:
    x = a.split(',')
    total += int(x[0]) * int(x[1])
print(total) # part 2: 102467299
