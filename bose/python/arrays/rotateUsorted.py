import time
def rotateArr(A,D,N):
    while D>0:
        first = A[0]
        last = A[N-1]
        for i in range(1,N-1):
            A[i-1] = A[i]
        A[N-2] = last
        A[N-1] = first 
        D-=1

    return A

if __name__ == "__main__":
    a =[2,4,6,8,10,12,14,16,18,20]
    N=  len(a)
    D = 3
    start = time.time()
    print(rotateArr(a,D,N))
    print(time.time()-start)