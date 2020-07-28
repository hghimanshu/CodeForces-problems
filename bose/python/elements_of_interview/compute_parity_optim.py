import time
def compute_party(x):
    result = 0
    while x:

        result^=1
        #  result+=result&x
        x&=(x-1)
    return result

t0 = time.time()
num = 6
print('The parity of the number '+str(num)+' is:: '+str(compute_party(num)))
t1 = time.time()
total = t1-t0
print(total)