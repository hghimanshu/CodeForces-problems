from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array: List[int] = [1 for i in range(len(nums))]
        suffix_array: List[int] = [1 for i in range(len(nums))]
        output_array: List[int] = [1 for i in range(len(nums))]
        
        prefix_array[0]=1
        prefix_array[1]=nums[0]*1
        
        suffix_array[len(nums)-1] = 1
        suffix_array[len(nums)-2] = nums[-1]
        
        for i in range(2,len(nums)):
            prefix_array[i] = prefix_array[i-1]*nums[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            suffix_array[i] = suffix_array[i+1]*nums[i+1]
            
        print(f"Prefix array is --> {prefix_array}")
        print(f"Suffix array is --> {suffix_array}")
        
        for i in range(0,len(nums)):
            output_array[i] = prefix_array[i]*suffix_array[i]
        
        return output_array
            
        
        
        
if __name__=="__main__":
    print(Solution().productExceptSelf([-1,1,0,-3,3]))
        
        
        