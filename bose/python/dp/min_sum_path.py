from functools import lru_cache
class Solution:

    
    def __init__(self):
        self.min_sum = float('inf')
        self.dirs = [(0,1),(1,0)]
        self.cache = {}


     

    def traverse_dp(self):


        row = [0]*self.cols

        dp =[]

        for i in range(0,self.rows):
            dp.append(row.copy())

        # print(dp)

        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if self.isValid(i-1,j) and self.isValid(i,j-1):
                    dp[i][j]= self.grid[i][j] +min(dp[i-1][j],dp[i][j-1])

                elif self.isValid(i-1,j):
                    dp[i][j]= self.grid[i][j] + dp[i-1][j]

                elif self.isValid(i,j-1):
                    dp[i][j] = self.grid[i][j]+ dp[i][j-1]
                
                else:
                    dp[i][j] = self.grid[i][j]

        print(dp)
        return dp[self.rows-1][self.cols-1]
        

    def traverse_memo(self,i,j):

        if i>= self.rows or i<0 or j<0 or j >= self.cols:
            return float('inf')
        
        if (i,j) in self.cache:
            return self.cache[(i,j)]

        if (i,j) == (self.rows-1,self.cols-1):
            return self.grid[i][j]

        cur_sum =0

        cur_sum = self.grid[i][j] + min(self.traverse_memo(i,j+1),self.traverse_memo(i+1,j))
        
        self.cache[(i,j)] = cur_sum 

        return cur_sum


    @lru_cache
    def traverse(self,i,j,curr_sum):
        if i>= self.rows or i<0 or j<0 or j >= self.cols:
            return

        curr_sum+=self.grid[i][j]
        # print(curr_sum)

        

        if (i,j) == (self.rows-1,self.cols-1):
            self.min_sum = min(curr_sum,self.min_sum)
            return

        for dx,dy in self.dirs:
            self.traverse(i+dx,j+dy,curr_sum)
        
    def minPathSum(self, grid):

        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        # self.traverse(0,0,0)

        # i,j=0,0
        # cur_sum =0
        # for dx,dy in self.dirs:
        #     cur_sum = self.traverse_memo(i+dx,j+dy)
        #     self.min_sum = min(self.min_sum, cur_sum)


        return self.traverse_dp()


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(sol.minPathSum(grid))