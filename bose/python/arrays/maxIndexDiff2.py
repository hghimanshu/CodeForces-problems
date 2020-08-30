def maxIndexDiff(a, n): 
    if n==0:
        return 0
    diff_arr = []
    i=0
    j=n-1

    while i<n:
        print("i is::: ",i)
        print("j is::: ",j)
        print("diff arr is::: ",diff_arr)
        if j==i:
            i+=1
            j=n-1
            continue
        if a[j] < a[i]:
            j-=1
            continue
        else:
            diff = j-i
            if diff_arr==[]:
                diff_arr.append(diff)
            if i>len(diff_arr)-1:
                diff_arr.append(diff)
            elif len(diff_arr)>0:
                if diff_arr[i] < diff:
                    diff_arr[i] = diff
            i+=1
            j=n-1
        
    
    # print(diff_arr)
    return max(diff_arr)




if __name__ == "__main__":
    import time
    start= time.time()
    # arr =[34,8,10,3,2,80,30,33,1]
    arr = [70, 83, 82, 39, 81]
    print(maxIndexDiff(arr,len(arr)))
    print(time.time()-start)    