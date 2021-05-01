class Solution:

    def __init__(self):
        pass


    def traverse(self,i,j,comb,word,idx):
        self.grid[i][j] = False
        if len(comb)==len(word):
            if "".join(comb)=="".join(word):
                return True
            return False

        if i < 0 or i>= self.rows or j < 0 or j >= self.cols :
            return 

        
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        for dx,dy in dirs:
            X,Y = i+dx,j+dy
            if X < 0 or X>= self.rows or Y < 0 or Y >= self.cols or self.grid[X][Y]!=word[idx+1] or not self.grid[X][Y]:
                continue
            else:
                comb.append(self.grid[X][Y])
                
                present = self.traverse(X,Y,comb,word,idx+1)
                if present:
                    return True  
                val =comb.pop()
                self.grid[X][Y] = val

        return False

    def exist(self, board, word):
        word_list = list(word)
        self.grid = board
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        word_found = False
        letter_found = False

        for i in range(0,self.rows):
            for j in range(0,self.cols):
                if self.grid[i][j]==word_list[0]:
                    word_found = self.traverse(i,j,[self.grid[i][j]],word_list,0)
                    self.grid[i][j] = word_list[0]
                if word_found:
                    break
            if word_found:
                break
        return word_found


    
if __name__ == "__main__":
    sol = Solution()
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(sol.exist(board,word))