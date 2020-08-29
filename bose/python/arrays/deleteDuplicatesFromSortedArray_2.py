def deleteDup(a):
    if not a:
        return 0
    
    wi=1
    for i in range(1,len(a)):
        if a[wi-1]!=a[i]:
            a[wi] = a[i]
            wi+=1

    print(a)
    return wi-1

if __name__ == "__main__":
    arr =[2,3,5,5,7,11,11,11,13]
    print(deleteDup(arr))