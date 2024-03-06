from typing import List

class Solution:
     
    def in_same_grid(self,idx,row,col):
        idx_grid_num =  (int(idx[0] / 3),int(idx[1]/3))
        row_col_num =  (int(row / 3),int(col /3))
        return idx_grid_num == row_col_num
        # if i
        # row_diff = row-idx[0]
        # col_diff =  col-idx[1]
        # if row_diff < 3 and row_diff > 0:
        #     if col_diff<3 and col_diff >0:
        #         return True 
        # else:
        #     return False
    
    def check_if_duplicate(self,idx_list:List,row:int,col:int):
        for idx in idx_list:
            if row==idx[0] or col==idx[1]:
                return True
            if self.in_same_grid(idx,row,col):
                return True
    
    def checkSudoku(self,board:List[List[str]]) -> bool:
        ### Create dict with grids       
        idx_dict = {}
        for row in range(0,len(board)):
            for col in range(0,len(board)):
                if (row==6 and col==3):
                    print("At the error")
                if board[row][col]==".":
                    continue
                if int(board[row][col]) > 9 or int(board[row][col]) < 1:
                    return False
                
                if idx_dict.get(board[row][col]):
                    if self.check_if_duplicate(idx_dict.get(board[row][col]),row,col):
                        print(idx_dict)
                        print(row,col)
                        return False
                    else:
                        idx_dict[board[row][col]].append((row,col))
                else:
                    idx_dict.update({board[row][col]:[(row,col)]})
        
        return True
                    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) !=9:
            return False
        return self.checkSudoku(board=board)
        
if __name__=="__main__":
    sudoku_board = [[".",".",".",".",".",".",".",".","."],
                    ["5",".",".",".",".",".",".",".","."],
                    [".","7","1",".",".",".","4",".","."],
                    [".",".",".",".",".",".",".",".","5"],
                    ["8","5",".",".",".","3",".",".","."],
                    [".",".","4",".",".","7",".","5","6"],
                    [".",".",".",".",".",".","8",".","."],
                    [".",".",".","2",".",".",".",".","."],
                    [".",".",".",".",".","6",".",".","."]]
    
    solution = Solution()
    print(solution.isValidSudoku(sudoku_board))
