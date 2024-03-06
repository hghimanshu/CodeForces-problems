from typing import List,Dict

class Solution:
    def __init__(self) -> None:
        self.index_to_zero_map: Dict = {}
    
    def _set_col_and_row_to_zero(self,src_i,src_j,matrix):
        
        def update_matrix(i,j,matrix):
            
            if matrix[i][j] == 0:
                if self.index_to_zero_map.get(str(i)+"_"+str(j),None):
                    pass
                # else:
                #     self.index_to_zero_map.update({str(i)+"_"+str(j):1})
            else:
                matrix[i][j] = 0
                self.index_to_zero_map.update({str(i)+"_"+str(j):1})
            
            return matrix
        
        for i in range(0,len(matrix)):
            matrix = update_matrix(i,src_j,matrix)
            
        for j in range(0,len(matrix[src_i])):
            matrix = update_matrix(src_i,j,matrix)
            
        return matrix
        
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 0:
                    if self.index_to_zero_map.get(str(i)+"_"+str(j),None):
                        continue
                    else:
                        self._set_col_and_row_to_zero(i,j,matrix=matrix)
                        self.index_to_zero_map.update({str(i)+"_"+str(j):1})
                        
        return matrix
    
if __name__=="__main__":
    sol = Solution()
    matrix = [[0,1]]
    print(sol.setZeroes(matrix=matrix))              
        