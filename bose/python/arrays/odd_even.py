def reorder_odd_even(arr):
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]%2!=0:
            if arr[j]%2==0:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
            j-=1
        else:
            i+=1

    return arr


arr = [2,4,6,8,5,3,9,11]
arr.reverse()
print("arr is:: ",arr)
print(reorder_odd_even(arr))