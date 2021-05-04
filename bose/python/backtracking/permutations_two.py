class Solution:

    def __init__(self):
        self.permutations = []
        self.numbers = {}
    

    def getPermutations(self,perm,nums,n):
        if len(perm)==n:
            self.permutations.append(perm.copy())
            return       

        
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            perm.append(nums[i])
            self.getPermutations(perm,nums[:i]+nums[i+1:],n)
            prev = perm.pop()

    
    def permute(self, nums):
        if len(nums) ==0:
            return []

        if len(nums) ==1:
            return [[nums[0]]]
        
        visited =[False]*len(nums)
        perm = []
        current =0
        n= len(nums)
        
        prev = -9999
        self.getPermutations([],nums,n)
        # for i in range(0,len(nums)):
        #     if nums[i]!=prev:
        #         visited[i]=True
        #         self.getPermutations(visited,[nums[i]],n,nums,prev)
        #         visited[i]=False
        #     prev = nums[i]
        return self.permutations


if __name__ == '__main__':
    nums = [3,3,0,3]
    sol = Solution()
    print(sol.permute(nums))