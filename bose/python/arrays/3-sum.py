def has_three_sum_with_hash(arr):
    arr.sort()
    num_hash = {}
    
    t = 0
    for i in arr:
        num_hash.update({i:1})
    
    triplet_list=set()
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            third_num = t-(arr[i]+arr[j])
            if num_hash.get(third_num):
                triplet_list.add((arr[i],arr[j],third_num))

    return triplet_list


def has_three_sum_with_two_pointer(nums):
    if not nums:
        return []
    elif len(nums) < 3:
        return []
    nums.sort()
    t=0
    triplet_list=set()
    for i in range(0,len(nums)):

        start = i+1
        end = len(nums) -1

        while start < end:
            if nums[start]+nums[end] == t-nums[i]:
                triplet_list.add((nums[i],nums[start],nums[end]))
                start+=1
                end-=1
            elif nums[start]+nums[end] < t-nums[i]:
                start+=1
            else:
                end-=1

    # return set(triplet_list)
    return list(triplet_list)


if __name__ == "__main__":
    arr = [-1,0,1,2,-1,-4]
    print("List of triplets are :: {}".format(has_three_sum_with_hash(arr)))
    