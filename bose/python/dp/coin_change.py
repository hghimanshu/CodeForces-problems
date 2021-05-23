# from functools import lru_cache
class Solution:

    def __init__(self):
        self.cache = {}
        self.min_change = float('inf')

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
        curr_min = float('inf')

        for change in self.changes:
            curr_min =min(curr_min,self.getChange(amount-change))
        
        if curr_min==float('inf'):
            return -1
        return curr_min
    
if __name__ == "__main__":
    coins = [2]
    amount = 3
    sol = Solution()
    print(sol.coinChange(coins, amount))