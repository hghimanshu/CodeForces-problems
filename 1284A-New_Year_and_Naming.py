import itertools

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
def lcm(a,b): 
    return (a*b) / gcd(a,b) 

if __name__ == "__main__":
    n, m = map(int, input().split(' '))
    s1 = list(map(str, input().split(' ')))
    s2 = list(map(str, input().split(' ')))
    q = int(input())
    total_queries = []
    for i in range(q):
            total_queries.append(int(input()))
    
    s1 = list(itertools.chain.from_iterable(itertools.repeat(s1, m)))
    s2 = list(itertools.chain.from_iterable(itertools.repeat(s2, n)))
    final_list = [i + j for i, j in zip(s1,s2)]
    lcm_ = lcm(n,m)
    for i in total_queries:
        i = i%int(lcm_)
        print(final_list[i-1])
    