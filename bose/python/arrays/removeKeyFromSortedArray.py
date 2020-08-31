def removeKey(a,key):
    if not a:
        return 0

    i=1
    wi=0
    while i<len(a):
        if a[wi]==key:
            a[wi]=a[i]

        else:
            w+1