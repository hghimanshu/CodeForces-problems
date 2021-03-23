def has_four_sum_with_two_pointer(nums):
    if not nums:
        return []
    elif len(nums) < 4:
        return []
    nums.sort()
    target=0

    triplet_list=set()
    for j in range(0,len(nums)):
        for i in range(j+1,len(nums)):
            t = target-nums[j]
            start = i+1
            end = len(nums) -1

            while start < end:
                if nums[start]+nums[end] == t-nums[i]:
                    triplet_list.add((nums[j],nums[i],nums[start],nums[end]))
                    start+=1
                    end-=1
                elif nums[start]+nums[end] < t-nums[i]:
                    start+=1
                else:
                    end-=1

                prev_start = start
                while start < end and start!=prev_start:
                    start+=1
                    prev_start=start
                
                prev_end = end
                while end > start and end!=prev_end:
                    end-=1
                    prev_end=end

            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1

        while j+1<len(nums) and nums[j+1]==nums[j]:
                j+=1

        # return set(triplet_list)
    return list(triplet_list)

if __name__ == "__main__":
    arr = [1,0,-1,0,-2,2]
    print("List of quaruples are :: {}".format(has_four_sum_with_two_pointer(arr)))
    