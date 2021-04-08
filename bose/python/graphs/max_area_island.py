class Solution:
    

    def __init__(self):
        self.max_area=0
        self.curr_area=0
    def maxIslandArea(self,grid):
        rows = len(grid)
        if rows == 0:
            return 0 #no islands because grid is empty
        cols = len(grid[0])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    if i==3:
                        print("At the 3rd row")
                    self.markCurrentIsland(grid,i,j,rows,cols)
                    if self.curr_area>=self.max_area:
                        self.max_area = self.curr_area
                    self.curr_area =0
        
        return self.max_area


    def markCurrentIsland(self,grid,i,j,rows,cols):
        if (i<0) or (i>=rows) or (j<0) or (j>=cols) or (grid[i][j]!=1):
            return 
        grid[i][j] =2
        self.curr_area+=1
        self.markCurrentIsland(grid,i+1,j,rows,cols)
        self.markCurrentIsland(grid,i,j+1,rows,cols)
        self.markCurrentIsland(grid,i-1,j,rows,cols)
        self.markCurrentIsland(grid,i,j-1,rows,cols)


if __name__ == "__main__":
    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    #     ]
    # grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    #     ]

    grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    obj = Solution()
    print("Max area is :: {}".format(obj.maxIslandArea(grid)))