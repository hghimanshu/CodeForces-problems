class Solution:
    def __init__(self):
        self.sets = []


    def getSubset(self,idx,curr_comb,nums):
        if idx>=len(nums):
            return

        curr_comb.append(nums[idx])
        self.sets.append(curr_comb.copy())

        for i in range(idx+1,len(nums)):
            self.getSubset(i,curr_comb,nums)
            curr_comb.pop()
    
    def subset(self,nums):
        for i in range(0,len(nums)):
            self.getSubset(i,[],nums)

        self.sets.append([])

        return self.sets

if __name__ == "__main__":
    sol = Solution()
    nums = [0]
    print("All subsets are:: {}".format(sol.subset(nums)))
        