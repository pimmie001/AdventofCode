import re

with open('13.txt') as fh:
    content = fh.read().split('\n\n')

machines = []
for text in content:
    numbers = re.findall(r'\d+', text)
    numbers = list(map(int, numbers))
    machines.append(numbers)



def is_close_to_integer(num, tolerance=1e-6):
    """Check if num is close to integer"""
    return abs(num - round(num)) <= tolerance 


total = 0
total2 = 0
for a,c,b,d,e,f in machines:
    ## part 1
    # Solve using linear algebra
    A = (d*e - b*f) / (a*d - c*b)
    B = (-c*e + a*f) / (a*d - c*b)

    if min(A,B) > 0 and is_close_to_integer(A) and is_close_to_integer(B):
        total += 3*round(A) + round(B)

    ## part 2
    e += 10000000000000
    f += 10000000000000

    # Solve using linear algebra
    A = (d*e - b*f) / (a*d - c*b)
    B = (-c*e + a*f) / (a*d - c*b)

    if min(A,B) > 0 and is_close_to_integer(A) and is_close_to_integer(B):
        total2 += 3*round(A) + round(B)

print(total) # part 1: 27105
print(total2) # part 2: 101726882250942