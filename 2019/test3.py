def f(A):
    if isinstance(A,list):
        result = f(A[0])                            # we kunnen niet in 1 keer return f(A[0]) doen omdat bij de depth er 1 moet worden opgeteld
        return result[0] , result[1] + 1             # de result[0] is dus het getal maar dan met 1 list minder.
                                                    # de result[1] is de diepte die hij tot nu was, die verhogen we dus met 1
    return A, 0         # dus als A zelf een integer is return hij de integer en 0 omdat dat de depth is

def g(B):
    if isinstance(B[0],list):
        result = g(B[0])
        return result[0] , result[1] + 1
    return B[0], 1





A=[[[[3]]]]

print(f(A))
print(g(A))
