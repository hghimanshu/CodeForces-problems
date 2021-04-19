class MaxPath:
    def __init__(self,grid):
        self.max_sequence = []
        self.max_length =0
        self.grid = grid
        self.cache={}

    def getMaxSeq(self):

        self.rows = len(self.grid)
        if self.rows==0:
            return 0

        self.cols =len(self.grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                self.checkPath(i,j,-999999)

        return self.max_length


    def checkPath(self,i,j,val): 
        if (i<0) or (i>=self.rows) or (j<0) or (j>=self.cols) or (self.grid[i][j]<=val):
            return 0

        temp = 1
        if (i,j) in self.cache:
            return self.cache[(i,j)]

        

        temp = max(temp,1+self.checkPath(i+1,j,self.grid[i][j]))
        temp = max(temp,1+self.checkPath(i-1,j,self.grid[i][j]))
        temp = max(temp,1+self.checkPath(i,j+1,self.grid[i][j]))
        temp = max(temp,1+self.checkPath(i,j-1,self.grid[i][j]))

        self.cache[(i,j)] = temp

        self.max_length = max(self.max_length,temp)

        return temp




    def getMaxSeqMemo(self):

        self.rows = len(self.grid)
        if self.rows==0:
            return 0

        self.cols =len(self.grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                self.checkPathMemo(i,j)

        return self.max_length

    def checkPathMemo(self,i,j):
        temp = 1

        dirs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

        if (i,j) in self.cache:
            return self.cache[(i,j)]

        for dx,dy in dirs:
            if dx>=0 and dx<self.rows and dy>=0 and dy<self.cols and self.grid[dx][dy] > self.grid[i][j]:
                temp = max(temp,self.checkPathMemo(dx,dy)+1)

        self.cache[(i,j)] = temp
        self.max_length = max(self.max_length,temp)

        return temp

if __name__ == "__main__":
    # matrix = [[9,9,4],[6,6,8],[2,1,1]]
    # matrix = [[3,4,5],[3,2,6],[2,2,1]]
    # matrix =  [[1]]
    matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    mp = MaxPath(matrix)
    print(mp.getMaxSeq())