class Solution:

    def __init__(self):
        self.permutations = []
        self.numbers = {}

    def swap(self,i,j,nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums
    
    def getPermutations(self,idx,nums,n):
        self.permutations.append(nums.copy())

        
        for i in range(idx+1,n):
            if i+1==n:
                continue
            nums = self.swap(i+1,idx+1,nums)
            self.getPermutations(idx+1,nums,n)
            nums = self.swap(idx+1,i+1,nums)
        return
        

    def permute(self,nums):
        n = len(nums)
        self.getPermutations(1,nums,n)
        return self.permutations

if __name__ == "__main__":
    sol = Solution()
    nums =  [1,2,3]

    print(sol.permute(nums))