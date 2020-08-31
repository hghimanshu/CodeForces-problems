def find3number(A, n):
    min =0
    max = n-1
    smaller = [0]*n
    greater = [0]*n

    smaller[0] = -1
    for i in range(1,n):
        if A[i]<=A[min]:
            min = i
            smaller[i]=-1
        else:
            smaller[i] = min

    greater[n-1] = -1
    for i in range(n-2,-1,-1):
        if A[i]>=A[max]:
            max = i
            greater[i] = -1
        else:
            greater[i]= max

    print(smaller)
    print(greater)

    for i in range(n):
        if smaller[i]!=-1 and greater[i]!=-1:
            return [A[smaller[i]],A[i],A[greater[i]]]
            # return 1
    return []

if __name__ == "__main__":
    a =[1,2,1,1,3]
    print(find3number(a,len(a)))