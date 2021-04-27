class Solution:

    def __init__(self):
        self.max_gold = 0

    def getGold(self,grid,i,j,visited):
        if i < 0 or i>= self.rows or j<0 or j>=self.cols or grid[i][j]==0:
            return 0
        
        current_gold = grid[i][j]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        new_gold =0
        for dx,dy in dirs:
            X,Y = i+dx,j+dy
            if not visited.get((X,Y),False):
            # if (X,Y) in visited:
            #     if visited[(X,Y)] == True:
            #         continue
            #     visited[(X,Y)] = True
            #     new_gold= max(new_gold,self.getGold(grid,X,Y,visited))
            #     visited[(X,Y)] = False
            # else:
                visited[(X,Y)] = True
                new_gold= max(new_gold,self.getGold(grid,X,Y,visited))
                visited[(X,Y)] = False
        visited[(i,j)] = False
        current_gold+=new_gold
        self.max_gold = max(self.max_gold,current_gold)

        return current_gold
            



    def getMaximumGold(self, grid):
        visited={}
        rows = len(grid)
        cols = len(grid[0])
        self.rows = rows
        self.cols = cols

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j]==0:
                    visited[(i,j)]=True
                    continue
                visited[(i,j)]=True
                self.getGold(grid,i,j,visited)
                visited[(i,j)] = False
        
        return self.max_gold


if __name__ == "__main__":
    # grid = [[0,6,0],[5,8,7],[0,9,0]]
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    sol = Solution()
    print(sol.getMaximumGold(grid))

                    
