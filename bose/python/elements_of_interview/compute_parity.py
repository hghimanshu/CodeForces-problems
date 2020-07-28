import time
def parity_brute(x):
    result = 0
    while(x):
        result ^=x&1
        x>>=1
    return result

t0 = time.time()
num = 2**32
print('Parity of the number is::'+str(parity_brute(num)))
t1 = time.time()
total = t1-t0
print(total)