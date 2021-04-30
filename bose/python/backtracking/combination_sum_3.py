class Solution:
    def __init__(self):
        self.sets= []
        self.nums = [i for i in range(1,10)]

    def getComb(self,comb,idx,k,n):

        if len(comb)==k and sum(comb)==n:
            self.sets.append(comb.copy())

        if len(comb)>k:
            return

        for i in range(idx+1,len(self.nums)):
            comb.append(self.nums[i])
            self.getComb(comb,i,k,n)
            comb.pop()

    def combinationSum3(self, k,n):
        for i in range(0,len(self.nums)):
            self.getComb([self.nums[i]],i,k,n)

        return self.sets


if __name__ == "__main__":
    sol = Solution()
    k=9
    n=45

    print(sol.combinationSum3(k,n))