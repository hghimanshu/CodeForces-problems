from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return len(nums)
        num_dict = {i:1 for i in nums}
        print(num_dict)
        if len(num_dict) == 1:
            return 1

        lcs = []
        longest = 0
        for num in nums:
            if not num_dict.get(num-1,None):
                length = 0
                while num_dict.get(num+length,None):
                    length+=1
                longest = max(longest,length)
        return longest
                    
        
if __name__=="__main__":
    sol = Solution()
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    print(sol.longestConsecutive(nums))