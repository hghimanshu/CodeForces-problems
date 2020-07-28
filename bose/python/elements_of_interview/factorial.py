
def fib(n):
    a=[]
    a.append(1)
    a.append(1)
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n-1]

if __name__ == "__main__":
    print(fib(6))

