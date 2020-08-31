def applyPerm(a,p):
    b=[0]*len(a)
    for i in range(0,len(a)):
        b[p[i]] = a[i]

    print(b) 


if __name__ == "__main__":
    a = ["a","b","c","d"]
    p = [3,1,2,0]
    applyPerm(a,p)
