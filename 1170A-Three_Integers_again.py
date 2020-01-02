def findValues(x, y):
    a = 1 ## as we have to minimize the values
    b = x -a
    c = y -b
    return a, b, c

if __name__ == "__main__":
    q = int(input())
    for i in range(q):
        x, y = map(int, input().split(' '))
        if x > y:
            x, y = y, x
        a, b, c = findValues(x, y)
        print(a,b,c)