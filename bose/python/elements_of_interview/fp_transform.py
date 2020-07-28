def transform(init,mapping,combination,seq):
    if not seq:
        return init
    else:
        return combination(mapping(seq[0]),transform(init,mapping,combination,seq[1:]))

def product_with_transform(seq):
    return transform(1,lambda x:x,lambda a,b:a*b,seq)

def sum_with_transform(seq):
    return transform(0,lambda x:x,lambda a,b: a+b,seq)


#reduction function (foldr)
def foldr(func,init,seq):
    if not seq:
        return init
    else:
        return func(seq[0],foldr(func,init,seq[1:]))

def product_with_foldr(seq):
    return foldr(lambda seqval,acc:seqval*acc,1,seq)

def sum_with_foldr(seq):
    return foldr(lambda seqval,acc:seqval+acc,0,seq)

def reverse_with_foldr(seq):
    return foldr(lambda seqval,acc:acc+[seqval],[],seq)

def foldl(func,init,seq):
    if not seq:
        return init
    else:
        return foldl(func,func(init,seq[0]),seq[1:])

def product_with_foldl(seq):
    return foldl(lambda seqval,acc:seqval*acc,1,seq)

def digits2num_with_foldl(seq):
    return foldl(lambda acc,seqval: acc*10 + seqval,0 ,seq)


if __name__ == "__main__":
    print(product_with_transform([1,2,3,4]))
    print(sum_with_transform([1,2,3,4]))
    print(product_with_foldr([1,2,3,4]))
    print(sum_with_foldr([1,2,3,4]))
    print(reverse_with_foldr([1,2,3,4]))
    print(product_with_foldl([1,2,3,4]))
    print(digits2num_with_foldl([1,2,3,4]))