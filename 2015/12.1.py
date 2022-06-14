with open("12.txt") as fh:
    content = fh.read().split("\n")


grandtotal = 0
for x in content:
    i = 0
    while i < len(x):
        minus = False
        number = ""
        if x[i].isnumeric():
            if i != 0 and x[i-1] == "-":
                minus = True
            while x[i].isnumeric():
                number += x[i]
                i += 1
                if i >= len(x):
                    break

        if number.isnumeric():
            if minus:
                grandtotal -= int(number)
            else: 
                grandtotal += int(number)
        i += 1

print(grandtotal) # 111754