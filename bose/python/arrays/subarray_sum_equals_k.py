def subarraySum(nums, k):
    sum_freq = {0:1}
    t = 0
    s=0
    for i in range(0,len(nums)):
        s+=nums[i]
    # for s in accumulate(nums):
        search_val = s-k
        t += sum_freq.get(search_val, 0)
        sum_freq[s] = sum_freq.get(s, 0) + 1
    return t

if __name__ == '__main__':
    # nums = [1,-1,0]
    nums = [1,2,1,2,1]
    # nums = [0,0,0,0,0]
    k = 3
    print(subarraySum(nums,k))