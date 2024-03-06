from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1000000
        sum = 0
        for item in nums:
            sum+=item
            if sum<=0:
                max_sum = max(sum,max_sum)
                sum = 0
            else:
                max_sum =  max(sum,max_sum)
                
        return max_sum
    
if __name__=="__main__":
    sol = Solution()
    print(sol.maxSubArray([-1,-2,-3]))