def backtrack(candidates,target,res,comb,idx):
    if target==0:
        res.append(comb.copy())

    for i in range(idx,len(candidates)):
        if candidates[i]<=target:
            if i==idx or candidates[i]!=candidates[i-1]:
                comb.append(candidates[i])
                backtrack(candidates,target-candidates[i],res,comb,i+1)
                comb.pop()




def combinationSum2(candidates,target):
    res= []
    comb= []
    candidates.sort()
    backtrack(candidates,target,res,comb,0)

    return res

if __name__=='__main__':
    candidates = [2,5,2,1,2]
    target = 5
    print(combinationSum2(candidates, target))