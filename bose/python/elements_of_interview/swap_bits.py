def swap_bits(x,i,j):
    if ((x>>i)&1) != ((x>>j)&1):
        #ith and jth are different. Use mask to change bit value
        bit_mask = (1<<i)|(1<<j)
        x^=bit_mask
    return x

if __name__ == "__main__":
    print('Swapped ::'+str(swap_bits(73,1,6)))