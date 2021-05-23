class Solution:

    def __init__(self):
        self.cache = {}


    def getCherry(self,src,dst,dirs):
        row = [0]*self.cols

        dp =[]

        for i in range(0,self.rows):
            dp.append(row.copy())

        i,j = src
        while i>=0 and i<self.rows and j<self.cols and j>=0:
            


            if self.grid[i+dirs[0][0]][j+dirs[0][1]] > self.grid[i+dirs[1][0]][j+dirs[1][1]]:
                if self.grid[i][j]==1:
                    self.dp[i][j]=2
                    self.grid[i][j]=0
                i+= dirs[0][0]
                j+= dirs[0][1]

            else:
            

    def traverse(self,i,j,dest_i,dest_j,dirs):

        if i<0 or i>=self.rows or j <0 or j>=self.cols or self.grid[i][j]==-1:
            return -1
        
        if (i,j) in self.cache:
            return self.cache[(i,j)]

        if (i,j) == (dest_i,dest_j):
            if self.grid[i][j] ==0:
                return 0
            elif self.grid[i][j]==1:
                self.grid[i][j]=0
                return 1
        
        totalVal = 0

        totalVal = self.grid[i][j]  + max(self.traverse(i+dirs[0][0],j+dirs[0][1],dest_i,dest_j,dirs),self.traverse(i+dirs[1][0],j+dirs[1][1],dest_i,dest_j,dirs))

        self.cache[(i,j)] = totalVal
        self.grid[i][j] = 0
        return totalVal

    
    def cherryPickup(self, grid):

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        numCherries=0
        #first traversal
        dirs = [(0,1),(1,0)]
        dest_i,dest_j = self.rows-1,self.cols-1

        numCherries+= self.traverse(0,0,dest_i,dest_j,dirs)
        
        print("Grid after first traversal")
        print(self.grid)
         #second traversal
        dirs = [(0,-1),(-1,0)]
        dest_i,dest_j = 0,0

        numCherries+= self.traverse(self.rows-1,self.cols-1,dest_i,dest_j,dirs)
        print("Grid after second traversal")
        print(self.grid)

        if numCherries > 0 and self.grid[self.rows-1][self.cols-1]==0:
            return numCherries
        elif numCherries==0 and self.grid[self.rows-1][self.cols-1]==0:
            return numCherries
        elif self.grid[self.rows-1][self.cols-1]!=0:
            return 0



if __name__ == '__main__':
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]

    sol = Solution()
    print(sol.cherryPickup(grid))



