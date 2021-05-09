from functools import lru_cache
class Solution:



    def jump_dp(self,n):
        dp = [0]*n

        dp[n-1],dp[n-2] = self.cost[n-1],self.cost[n-2]

        for i in range(n-3,-1,-1):
            dp[i]= cost[i] + min(dp[i+1],dp[i+2])
        
        return min(dp[0],dp[1])

    @lru_cache
    def jump(self,index):

        if index >=self.n:
            return 0

        
        totalCost = self.cost[index]+min(self.jump(index+1),self.jump(index+2))

        return totalCost

    def minCostClimbingStairs(self, cost):
        self.n = len(cost)
        self.cost = cost
        # return min(self.jump(0),self.jump(1))

        return self.jump_dp(self.n)

    
    
if __name__ == "__main__":
    cost = [10,15,20]

    sol = Solution()

    print(sol.minCostClimbingStairs(cost))