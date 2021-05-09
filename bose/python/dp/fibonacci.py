def fib_rec(n):
    if n==0 or n==1:
        return 1

    else:
        return fib(n-1) + fib(n-2)


def fib_memo(n,memo):
    if n in memo:
        return memo[n]
    if n==0 or n==1:
        return 1

    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo) #saving val in memo object
    return memo[n]


def fib_dp(n): 
    fib = []
    for i in range(0,n):
        if i==0 or i==1:
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]


if __name__ == '__main__':
    n = 49
    print(fib_memo(n,{}))