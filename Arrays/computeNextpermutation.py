def nextPermutation(A):
    inversion_point = len(A) - 2
    while inversion_point >= 0 and A[inversion_point] >=A[inversion_point +1]:
        inversion_point -= 1
    
    if inversion_point == -1:
        return []
    for i in reversed(range(inversion_point + 1, len(A))):
        if A[i] > A[inversion_point]:
            A[inversion_point], A[i] = A[i], A[inversion_point]
            break
    
    A[inversion_point + 1:] = reversed(A[inversion_point + 1:])
    return A



A = [1,0,3,2]
# A = [3,2,1,0]

print(nextPermutation(A))