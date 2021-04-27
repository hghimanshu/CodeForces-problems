class Solution:
    def __init__(self):
        self.sets= []


    def getComb(self,idx,curr,nums,target,prev):
        if sum(curr)>target:
            return

        if sum(curr)==target:
            self.sets.append(curr.copy())
            return
        # prev= nums[idx]
        for i in range(idx+1,len(nums)):
            if nums[i]!=prev:
                curr.append(nums[i])
                self.getComb(i,curr,nums,target,prev)
                prev = curr.pop()
            # prev=nums[i]
            
    def combinationSum2(self,candidates,target):
        candidates.sort()
        prev= 0
        for i in range(0,len(candidates)):
            if candidates[i]!=prev:
                self.getComb(i,[candidates[i]],candidates,target,0)
            prev = candidates[i]
        
        return self.sets

if __name__ == "__main__":
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(sol.combinationSum2(candidates, target))