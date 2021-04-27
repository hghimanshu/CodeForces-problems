class Solution:

    def __init__(self):
        self.combinations = []
        self.checked = {}

    def getCombinations(self,candidates,curr,target,idx):

        if target - sum(curr) ==0:
        # if sum(curr) == target:
            # sorted_curr = sorted(curr)
            # sorted_str = "".join(str(k) for k in sorted_curr)
            # if sorted_str not in self.checked:
                                                                                                       
            self.combinations.append(curr.copy()) 
                # self.checked[sorted_str] = 1
            return
        if sum(curr) > target:
            return

        for j in range(idx+1,len(candidates)):
            if candidates[j] > (target - sum(curr)):
                return
            new_num = curr + [candidates[j]]
            self.getCombinations(candidates,new_num,target,j)
            


    def combinationSum2(self, candidates, target):
        candidates.sort()
        prev= 0
        for i in range(0,len(candidates)):
            # diff = target - candidates[i
            if candidates[i]!=prev:
                self.getCombinations(candidates,[candidates[i]],target,i)
            prev = candidates
        
        return self.combinations

if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    sol = Solution()
    print(sol.combinationSum2(candidates, target))