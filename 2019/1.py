with open("1.txt") as fh:
    content=fh.read().split("\n")

def fual(n):
    return n//3-2

total=0
for n in content:
    total+=fual(int(n))
print(total)    # answer part 1: 3342351

def fual2(n):
    result=0
    number=n//3-2
    if number <= 0:
        return 0
    else: 
        result+= number + fual2(number)
    return result

total2=0
for n in content:
    total2+=fual2(int(n))
print(total2)    # answer part 2: 5010664