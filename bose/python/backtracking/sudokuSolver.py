class Solution:
    
    def isValid(self,num,row,col,board):
        grid = {}
        #row check
        for i in range(0,self.rows):
            if board[i][col]==num:
                return False


        #col check
        for j in range(0,self.cols):
            if board[row][j]==num:
                return False

        #grid check
        row_offset = (row // 3)*3
        col_offset = (col // 3)*3

        for i in range(0,3):
            for j in range(0,3):
                X = i+row_offset
                Y = j+col_offset
                if board[X][Y]!=".":
                    if board[X][Y]==num:
                        return False
        return True

    
    def solve(self,board,idx,cell):
        if idx==len(cell):
            return True

        X,Y = cell[idx]
        
        
        for x in range(1,10):
            num = str(x)
            if self.isValid(num,X,Y,board):
                board[X][Y] =num
                if self.solve(board,idx+1,cell):
                    return True
                board[X][Y] = "."
        
        return False




    def solveSudoku(self,board):
        self.rows = len(board)
        self.cols = len(board[0])

        cell = []
        for i in range(0,self.rows):
            for j in range(self.cols):
                if board[i][j]==".":
                    cell.append((i,j))
        
        self.solve(board,0,cell)

        print(board)


if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)
