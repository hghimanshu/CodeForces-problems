class Solution:


    def __init__(self):
        self.boards =[]


    def insertBoard(self,board):
        new_board = []
        for i in board:
            new_board.append("".join(i))
        
        self.boards.append(new_board)

    def isValid(self,board,x,y,n):
        ##check column
        for i in range(0,x):
            if board[i][y]=="Q":
                return False
        
        ##check left diagonal

        i=x-1
        j=y-1
        while j>=0 and i>=0:
            if board[i][j]=="Q":
                return False
            j-=1
            i-=1

        
        #check the right diagonal
        i=x-1
        j=y+1
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1

        return True

    
    def solve(self,board,i,num):
        if i==num:
            self.insertBoard(board.copy())
            return
        
        for j in range(0,n):
            if self.isValid(board,i,j,n):
                board[i][j] = "Q"
                self.solve(board,i+1,num)
                board[i][j] = "."

        return

    def solveNQueens(self, n):
        row =["."]*n
        board = [row.copy() for i in range(0,n)]
        # print(board)
        self.solve(board,0,n)

        return self.boards

if __name__ == "__main__":
    sol = Solution()
    n=4
    print(sol.solveNQueens(n))