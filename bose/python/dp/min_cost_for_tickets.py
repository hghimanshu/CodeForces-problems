from functools import lru_cache
class Solution:

    def __init__(self):
        self.cache = {}
        self.min_change = float('inf')

    @lru_cache
    def travel(self,day,end):

        if day > end:
            return 0

        
        if day not in self.days:
            return self.travel(day+1,end)


        curr_min = float('inf')

        for i,cost in self.costs.items():
            # print(i,cost)
            curr_min = min(curr_min,cost+self.travel(day+i,end))


        return curr_min


    def mincostTickets(self, days, costs):
        self.days = set(days)

        self.costs = {1:costs[0],7:costs[1],30:costs[2]}
        
        return self.travel(1,max(self.days))

if __name__ == "__main__":
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    sol = Solution()
    print(sol.mincostTickets(days,costs))