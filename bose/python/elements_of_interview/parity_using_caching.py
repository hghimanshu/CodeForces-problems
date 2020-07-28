import time
def precomputed_parity(x):
    result = 0
    while x:
        result^=1
        x&=(x-1)
    return result

def compute_parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return precomputed_parity(x>>(3*MASK_SIZE))^precomputed_parity((x>>(2*MASK_SIZE))&BIT_MASK)^precomputed_parity((x>>MASK_SIZE)&BIT_MASK)^precomputed_parity(x&BIT_MASK)
    # return parity_result
    


if __name__ == "__main__":
    t0=time.time()
    num = 2**32
    print('parity of '+str(num)+' is '+str(compute_parity(num)))
    t1=time.time()
    print('Time taken is::'+str(t1-t0))