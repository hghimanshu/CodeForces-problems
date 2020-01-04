import itertools

def checkJoy(a, b):
    joy = 0

    for i in range(len(a)):
        inna = list(range(1, a[i] +1))
        dima = list(range(1, a[i] +1))
        val = list(itertools.product(inna, dima))
        val = [j for j in val if sum(j) == b[i]]
        if len(val) == 0:
            joy -=1
        else:
            val = sorted(val, reverse=True,key=lambda x:(x[0]*x[1]))[0]
            joy += val[0]*val[1]
    return joy

if __name__ == "__main__":
    # n = int(input())
    # a = list(map(int, input().split(' ')))
    # b = list(map(int, input().split(' ')))
    n = 10
    a = [10000, 10000, 10000]
    b = [5000, 5000, 1]
    ans = checkJoy(a, b)
    print(ans)