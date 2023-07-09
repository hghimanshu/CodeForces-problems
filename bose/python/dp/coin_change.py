# from functools import lru_cache
class Solution:

    def __init__(self):
        self.cache = {}
        self.min_change = float('inf')

    def getChangeDp(self,sum):
        dp = [sum+1]*(sum+1)

        dp[0] = 0
        for i in range(1,len(dp)):
            for change in self.changes:
                aux_val = i-change
                if aux_val <0:
                    continue
                dp[i] = min(dp[aux_val]+1,dp[i])
        
        return dp[sum]



    # @lru_cache
    def getChange(self,sum):
        
        if sum == 0:
            return 1

        elif sum <0:
            return float('inf')
        
        elif sum in self.cache:
            return self.cache[sum]

        
        curr_min = float('inf')

        for change in self.changes:
            curr_min = min(curr_min,self.getChange(sum-change))
        
        self.cache[sum] = curr_min+1

        return curr_min+1


    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        self.changes = coins
        # curr_min = float('inf')

        # for change in self.changes:
        #     curr_min =min(curr_min,self.getChange(amount-change))
        
        curr_min = self.getChangeDp(amount)
        if curr_min == amount+1:
            return -1
        return curr_min
        
       
    
if __name__ == "__main__":
    coins = [2]
    amount = 3
    sol = Solution()
    print(sol.coinChange(coins, amount))