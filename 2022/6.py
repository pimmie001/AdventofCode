with open('6.txt') as fh:
    string = fh.read()

n = 14 # choose 4 or 14 for part 1/2
for i in range(len(string)-n):
    substring = string[i:i+n]
    if len(substring) == len(set(substring)):
        print(i+n) # part 1: 1848, part 2: 2308
        break
