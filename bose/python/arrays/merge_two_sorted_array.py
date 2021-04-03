def merge(nums1,nums2,m,n):

    if nums2==[]:
        return nums1
    

    i=0
    j=0
    
    last_index = m-1
    while i<m+n and i<=last_index and j<n:
        
        if nums1[i] <= nums2[j]:
            i+=1
            continue
        if nums1[i]>nums2[j]:
            nums1[i+1:] =  nums1[i:-1]
            nums1[i] = nums2[j]
            i+=1
            j+=1
            last_index+=1
        # if i==last_index:
        #     break
    i=last_index+1
    while i<m+n and j<n:
        nums1[i] = nums2[j]
        i+=1
        j+=1



if __name__ == "__main__":
    arr1 = [4,5,6,0,0,0]
    arr2 =  [1,2,3]
    print("Merged array is :: {}".format(merge(arr1,arr2,3,3)))
    