def findPrime(n):
    allPrime = []
    for num in range(1, n+1):
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            allPrime.append(num)
    return allPrime

def goodApproachPrime(n):
    primes = []
    is_prime = [False, False] + [True] * (n-1)

    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)

            for i in range(p, n+1, p):
                is_prime[i] = False
    return primes

n = 500000
# print(findPrime(n))
print(goodApproachPrime(n))