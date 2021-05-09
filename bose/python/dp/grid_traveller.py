class Solution:

    def __init__(self):
        self.total_paths = 0
        self.cache = {}


    def traverse(self,i,j,m,n):
        # if i< 0 or i>= self.rows or j < 0 or j >= self.cols:
        #     return
        
        if (i,j) == (m-1,n-1):
            self.total_paths+=1
            return

        dirs = [(0,1),(1,0)]

        for dx,dy in dirs:
            X,Y = i+dx,j+dy
            if X< 0 or X>= m or Y < 0 or Y >= n:
                continue
            self.traverse(X,Y,m,n)

    def traverse_memo(self,i,j,m,n):

        if (i,j) == (m-1,n-1):
            return 1

        if (i,j) in self.cache:
            return self.cache[(i,j)]

        pathSum = 0
        dirs = [(0,1),(1,0)]
        for dx,dy in dirs:
            X,Y = i+dx,j+dy
            if X< 0 or X>= m or Y < 0 or Y >= n:
                continue
            pathSum+=self.traverse_memo(X,Y,m,n)
        
        self.cache[(i,j)] = pathSum
        return self.cache[(i,j)]


    def gridTraveller(self,m,n):
        self.total_paths = self.traverse_memo(0,0,m,n)

        print(self.total_paths)
    
if __name__ == "__main__":
    sol = Solution()
    m=20
    n=20
    sol.gridTraveller(m,n)
