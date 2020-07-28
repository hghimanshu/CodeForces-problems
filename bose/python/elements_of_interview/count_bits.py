def count_bits(x):
    num_bits =0
    while x:
        num_bits+=x&1
        x>>=1
    return num_bits

num_to_count=6

print('num of bits in '+str(num_to_count)+' is::'+str(count_bits(num_to_count)))