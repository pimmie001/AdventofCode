def summation(x):
    if x>1:
        return summation(x-1) + x
    return x

def digits(n):
    if n >=10:
        return digits(n//10) + 1
    return 1

def fib1(n):        # langzaam bij getallen vanaf 30
    if n==0 or n==1:
        return n
    return fib1(n-2) + fib1(n-1)

def fib2(n):
    A=[0, 1]
    for i in range(n-1):
        A.append(A[i] + A[i+1])
    return A[n]

def fib3(n):        # rekenfout bij grote getallen (70+)
    import math as m
    phi = ( 1 + m.sqrt(5) ) / 2
    phi2= ( 1 - m.sqrt(5) ) / 2     # phi's little brother
    return round(( phi ** n - phi2 ** n) / m.sqrt(5))
    # return round((phi ** n)/m.sqrt(5))
