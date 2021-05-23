class Solution:

    def __init__(self):
        self.min_sum = float('inf')
        self.dirs = [(0,1),(1,0)]
        self.cache = {}


    def isValid(self,i,j):
        if i>= self.rows or i<0 or j<0 or j >= self.cols:
            return False
        return True


    def traverse_dp(self):

        row = [0]*self.cols 
        dp = []

        for i in range(0,self.rows):
            dp.append(row.copy())


        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if self.isValid(i-1,j) and self.isValid(i,j-1):
                    dp[i][j]= self.grid[i][j] +max(dp[i-1][j],dp[i][j-1])
                elif self.isValid(i-1,j):
                    dp[i][j]= self.grid[i][j] + dp[i-1][j]

                elif self.isValid(i,j-1):
                    dp[i][j] = self.grid[i][j]+ dp[i][j-1]
                
                else:
                    dp[i][j] = self.grid[i][j]

        print(dp)
        return dp[self.rows-1][self.cols-1]

    def getMinPath(self,i,j):
        if not self.isValid(i,j):
            return float('inf')

        if (i,j) == (self.rows-1,self.cols-1):
            return self.grid[i][j]
        if (i,j) in self.cache:
            return self.cache[(i,j)]

        cur_sum = 0

        cur_sum = self.grid[i][j] + min(self.getMinPath(i,j+1),self.getMinPath(i+1,j))
        self.cache[(i,j)] = cur_sum

        return cur_sum

    def calculateMinimumHP(self, dungeon):
        
        self.grid = dungeon
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])


        power_level = self.traverse_dp()
        if power_level > 0:
            return 1
        if power_level ==0:
            return 0

        else:
            return 1-power_level

if __name__ == "__main__":
    sol = Solution()
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(sol.calculateMinimumHP(dungeon))