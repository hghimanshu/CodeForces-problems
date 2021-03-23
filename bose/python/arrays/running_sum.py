def runningSum(nums):
    running_sum=[]
    for i in range(0,len(nums)):
        if i==0:
            running_sum.append(nums[i])
        else:
            running_sum.append(running_sum[i-1]+nums[i])
    return running_sum

if __name__ == "__main__":
    x = [1,2,3,4]
    print(runningSum(x))