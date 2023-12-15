with open('15.txt') as fh:
    string = fh.read()

# string = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7' # example

total = 0
for substring in string.split(','):
    val = 0
    for char in substring:
        val += ord(char)
        val *= 17
        val %= 256
    total += val
print(total)