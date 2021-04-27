class Solution:

    def __init__(self):
        self.totalPaths = 0
        self.cache = {}
        

    def traversePathMemoized(self,i,j,end):
        if i < 0 or i>= self.rows or j < 0 or j >= self.cols or self.grid[i][j]==1:
            return 0
        if (i,j) == end:
            # self.totalPaths+=1
            return 1
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        dirs = [(i,j+1),(i+1,j)] 
        dir1 = self.traversePathMemoized(i,j+1,end)
        dir2 = self.traversePathMemoized(i+1,j,end)

        self.cache[(i,j)]= dir1+dir2

        return dir1+dir2
       
    
    def uniquePathsWithObstacles(self,grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        # self.traverse(0,0,(m-1,n-1))
        return self.traversePathMemoized(0,0,(self.rows-1,self.cols-1))
        # return self.totalPaths
    

if __name__ == '__main__':
    
    obstacleGrid = [[0,1],[0,0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))

