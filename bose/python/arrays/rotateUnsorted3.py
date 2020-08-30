import time

def rotateArr(A,D,N):
    d= [0]*D
    for i in range(0,D):
        d[i] = A[i]
    
    for i in range(D,N):
        A[i-D] = A[i]
    
    for i in range(0,D):
        A[N-D+i] = d[i]
    
    return A

if __name__ == "__main__":
    a =[2,4,6,8,10,12,14,16,18,20]
    N=  len(a)
    D = 3
    start = time.time()
    print(rotateArr(a,D,N))
    print(time.time()-start)