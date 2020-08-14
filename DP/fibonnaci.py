def simpleFibonnaci(n):
    if n <= 1:
        return 1
    return simpleFibonnaci(n -1) + simpleFibonnaci(n-2)


def goodFibonnaci(n, cache={}):
    if n <=1:
        return 1
    
    elif n not in cache:
        cache[n] = goodFibonnaci(n-1) + goodFibonnaci(n-2)
    
    return cache[n] 

def dpApproach(n):
    if n <=1:
        return 1
    
    f2, f1 = 0, 1

    for _ in range(1, n+1):
        f = f2 + f1
        f2, f1 = f1, f
    
    return f1
# print(simpleFibonnaci(500))
# print(goodFibonnaci(500))
print(dpApproach(5000))