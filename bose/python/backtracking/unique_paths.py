class Solution:

    def __init__(self):
        self.totalPaths = 0
        self.cache = {}

    def traverse(self,i,j,end):
        if (i,j) == end:
            self.totalPaths+=1
            return
        dirs = [(i,j+1),(i+1,j)] 
        for X,Y in dirs:
            if X < 0 or X >= self.rows or Y < 0 or Y >= self.cols:
                continue
            self.traverse(X,Y,end)

    def traversePathMemoized(self,i,j,end):
        if i < 0 or i>= self.rows or j < 0 or j >= self.cols:
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
       
    
    def uniquePaths(self, m, n):
        self.rows = m
        self.cols = n
        # self.traverse(0,0,(m-1,n-1))
        return self.traversePathMemoized(0,0,(m-1,n-1))
        # return self.totalPaths
    

if __name__ == '__main__':
    m=3
    n=3
    sol = Solution()
    print(sol.uniquePaths(m,n))

