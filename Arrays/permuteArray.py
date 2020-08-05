def permutedArray(A, P):
    result  = [None] * len(A)

    for i in range(len(A)):
        pos = P[i]
        elem = A[i]
        result[pos] = elem
    
    return result



A = [5,6,7,8]
P = [3, 2,1, 0]

print(permutedArray(A, P))