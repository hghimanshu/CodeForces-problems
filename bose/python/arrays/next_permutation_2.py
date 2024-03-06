from typing import List

class Solution:
    
    def __init__(self) -> None:
        self.nums = []
    
    def _reverse_array(self,start_idx:int,end_idx:int):
        i: int = start_idx
        j: int = end_idx
        
        while(i<j):
            temp = self.nums[i]
            self.nums[i] = self.nums[j]
            self.nums[j] = temp
            i+=1
            j-=1
        
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## find the breakpoint (idx where arr[idx]<arr[idx+1])
        self.nums = nums
        if len(self.nums)==0 or len(self.nums)==1:
            return self.nums
        
        i = len(self.nums)-2
        while(i>-1):
            if self.nums[i+1]>self.nums[i]:
                break
            i-=1
        if i==-1:
            ##return reversed array
            return self._reverse_array(0,len(self.nums)-1)
        else:
            breakpoint_idx: int = i
            ##since entire array after breakpoint is in descending order
            ### we will swap first large element with self.nums[breakpoint_idx]
            for i in range(len(self.nums)-1,breakpoint_idx,-1):
                if self.nums[i] > self.nums[breakpoint_idx]:
                    ### perform swap operation
                    temp = self.nums[breakpoint_idx]
                    self.nums[breakpoint_idx] = self.nums[i]
                    self.nums[i] = temp
                    break
            
            print(f"Array after swapping with breakpoint : {self.nums}")
            ### now we will reverse the everything on the right side of the breakpoint index
            self._reverse_array(breakpoint_idx+1,len(self.nums)-1)
            # reversed_partition_array = self._reverse_array(nums[breakpoint_idx+1:])
            # print(f"Reversed partition array is {reversed_partition_array}")
            # initial_partition = nums[0:breakpoint_idx+1]
            # print(f"initial partition array is {initial_partition}")
            # return initial_partition + reversed_partition_array
            print(f"Next permutation is --->{self.nums}")

if __name__=="__main__":
    solution = Solution()
    nums = [1,3,2]
    solution.nextPermutation(nums)