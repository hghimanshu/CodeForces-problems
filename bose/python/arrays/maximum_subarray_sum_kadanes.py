def maxSubArray(nums):
    max =nums[0]
    sum = 0

    for i in range(0,len(nums)):
        sum+=nums[i]
        if sum > max:
            max = sum
        if sum<0:
            sum = 0
    return max

if __name__ == '__main__':
    arr = [-3,-2,0,-1]
    print("Maxium subarray sum is :: {}".format(maxSubArray(arr)))