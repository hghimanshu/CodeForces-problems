class Solution:

    def __init__(self):
        self.total_paths = 0
        self.cache = {}


    def climbBottomUp(self,n):

        dp = [0]*(n+1)    
        dp[0],dp[1] =1,1

        x,y = 1,1
        ans = 0
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        self.total_paths = dp[n]

    def climbMemo(self,comb,curr,target):

        if target < 0:
            return 0
        if target == 0:
            print(comb)
            return 1

        if (curr,target) in self.cache:
            print("cached valued is :: {}".format(self.cache[curr,target]))
            return self.cache[(curr,target)]

        total=0
        for i in range(1,3):
            if (target-i) >=0:
                comb.append(i)
                val=self.climbMemo(comb,i,target-i)
                comb.pop()
                self.cache[(i,target-i)]=val
                total+=val
                self.total_paths = max(self.total_paths,total)
        return total

    def climb(self,curr,target):

        if sum(curr) == target:

            self.total_paths+=1
            # print(",".join([str(x) for x in curr]))
            return
        
        if sum(curr) > target:
            return

        for i in range(1,3):
            curr.append(i)
            self.climb(curr,target)
            curr.pop()
    
    def climbStairs(self, n):

        self.climbBottomUp(n)

        return self.total_paths


if __name__ == '__main__':
    sol = Solution()

    print(sol.climbStairs(45))