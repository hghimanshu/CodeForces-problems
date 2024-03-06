from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## not inplace
        new_row = [0 for i in range(len(matrix[0]))]
        new_matrix = [new_row.copy() for i in range(len(matrix))]
        
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                new_matrix[i][j] = matrix[len(matrix)-1-j][i]
        return new_matrix
    
if __name__=="__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.rotate(matrix=matrix))
