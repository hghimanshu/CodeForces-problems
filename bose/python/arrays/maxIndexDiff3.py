def maxIndexDiff(a, n): 
    leftMin = [0]*n
    rightMax = [0]*n

    leftMin[0] = a[0]
    for i in range(1,n):
        leftMin[i] = min(a[i],leftMin[i-1])
    
    rightMax[n-1] = a[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i] = max(a[i],rightMax[i+1])

    print(leftMin)
    print(rightMax)

    i=0
    j=0
    maxDiff = -1
    # print(n)
    while i<n and j<n:
        if leftMin[i]<=rightMax[j]:
            maxDiff= max(maxDiff,j-i)
            # print(maxDiff)
            j+=1
        else:
            i+=1
            j+=1

    return maxDiff
    # return max(diff_arr)




if __name__ == "__main__":
    import time
    start= time.time()
    # arr =[34,8,10,3,2,80,30,33,1]
    arr = [82,63,44,74,82,99,82]
    
    print(maxIndexDiff(arr,len(arr)))
    print(time.time()-start)    