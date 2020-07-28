def deleteDuplicates(a):
    index=1
    for i in range(1,len(x)):
        if a[index-1]!=a[i]:
            a[index]=   a[i]
            index+=1
    print(a)

if __name__ == "__main__":
    x=[2,3,3,5,5,5,7,7,9,10,10]
    deleteDuplicates(x)