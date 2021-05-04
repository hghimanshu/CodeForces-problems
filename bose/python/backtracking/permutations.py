class Solution:

    def __init__(self):
        self.permutations = []
        self.numbers = {}
    
    def getPermutations(self,visited,perm,n,nums):
        if len(perm) == n:
            self.permutations.append(perm.copy())
            return

        for j in range(0,len(nums)):
            if not visited[j]:
                visited[j]=True
                perm.append(nums[j])
                self.getPermutations(visited,perm,n,nums)
                perm.pop()
                visited[j]=False
        

    
    def permute(self, nums):
        if len(nums) ==0:
            return []

        if len(nums) ==1:
            return [[nums[0]]]
        
        visited =[False]*len(nums)
        perm = []
        current =0
        n= len(nums)
        self.getPermutations(visited,perm,n,nums)
                

        return self.permutations


if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.permute(nums))

