def nextPermutation(nums):


    if len(nums)<=1 or nums == []:
        return

    

    i=len(nums)-2 #First breakpoint(Increasing to decreasing) can happen at second last index
    while i>=0 and nums[i]>= nums[i+1]:
        i-=1
    if i>=0:
        j = len(nums)-1 #need to find number greater than the number at which breakpoint occurs
        while nums[j] <=nums[i]:
            j-=1
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    m=i
    n = len(nums)-1

    while m <n :
        temp = nums[m+1]
        nums[m+1] = nums[n]
        nums[n] = temp
        m+=1
        n-=1
        
    print(nums)



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(nextPermutation(arr))


