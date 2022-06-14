def search(A):
    dimension=1
    if isinstance(A[0], list):
        result = search(A[0])
        return result[0], dimension + result[1]
    return A[0], dimension


def search2(A):
    if isinstance(A, list):
        result = search2(A[0])
        return result[0], result[1] + 1
    return A, 0


A=[[[420]]]
print(search2(A))