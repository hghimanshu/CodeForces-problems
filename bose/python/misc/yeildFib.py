def fib(n):
    a = 0
    b = 1
    for i in range(0,n):
        yield a
        total = a+b
        a = b
        b = total

for x in fib(10):
    print(x)    