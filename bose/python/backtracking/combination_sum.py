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

        for j in range(idx,len(candidates)):
            if candidates[j] > (target - sum(curr)):
                continue
            new_num = curr + [candidates[j]]
            self.getCombinations(candidates,new_num,target,j)

    def combinationSum(self, candidates, target):
        for i in range(0,len(candidates)):
            # diff = target - candidates[i]
            self.getCombinations(candidates,[candidates[i]],target,i)
        
        return self.combinations

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    sol = Solution()
    print(sol.combinationSum(candidates, target))



