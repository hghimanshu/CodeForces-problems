import random
random.seed(0)

def sampleData(a,k):
    for i in range(k):
        r = random.randint(i,len(a)-1)
        a[i],a[r] = a[r],a[i]
    
    print(a[:k])
    print(a)


if __name__ == "__main__":
    a = [3,7,5,6,2,9,8]
    sampleData(a,3)