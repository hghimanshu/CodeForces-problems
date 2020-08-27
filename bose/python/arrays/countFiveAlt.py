def convertFive(n):
    # Code here
    i=0
    finalNum=0
    if n>10000:
        return n
    while n>0:
        rem = n%10
        print("Rem is:: ",rem)
        n=int(n/10)
        multiplier=pow(10,i)
        print("multipler is:: ",multiplier)
        if rem==0:
            finalNum+= multiplier*5
        else:
            finalNum+= multiplier*rem
        print("Final num is:: ",finalNum)
        print("num is::: ",n)
        i+=1
    return finalNum



if __name__ == "__main__":
    print(convertFive(2054))