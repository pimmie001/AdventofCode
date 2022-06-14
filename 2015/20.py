from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


input = 29000000

### part 1
def presentscount(n):
    return 10 * sum(factors(n))


i = 1
while True:
    if presentscount(i) >= input:
        print(i)
        break
    i += 1


### part 2
def presentscount2(n):
    count = 0
    for divisor in factors(n): 
        if n // divisor <= 50:
            count += 11*divisor
    return count


i = 1
while True:
    if presentscount2(i) >= input:
        print(i)
        break
    i += 1
