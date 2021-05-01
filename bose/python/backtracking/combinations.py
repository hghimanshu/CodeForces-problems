class Solution:

    def __init__(self):
        self.sets = []


    def getCombinations(self,curr,k,idx,nums):

        if len(curr)==k:
            self.sets.append(curr.copy())
            return

        for i in range(idx+1,len(nums)):
            curr.append(nums[i])
            self.getCombinations(curr,k,i,nums)
            curr.pop()

    def combine(self, n, k):
        nums = [i for i in range(1,n+1)]
        for i in range(0,len(nums)):
            self.getCombinations([nums[i]],k,i,nums)

        return self.sets

if __name__ == "__main__":
    sol = Solution()
    n=1
    k=1
    print(sol.combine(n,k))