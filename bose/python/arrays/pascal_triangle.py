from typing import List

class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        row_list: List[List[int]] = []
        for row_num in range(0,numRows):
            if row_num == 0:
                row_list.append([1])
            elif row_num == 1:
                row_list.append([1,1])
            else:
                new_row: List[int] = [1]
                # prev_row: List[int] = row_list[row_num-1]
                ### Get row sum from prev row
                # row_idx: int = 0 
                # while row_idx < len(prev_row)-1:
                #     new_row.append(prev_row[row_idx]+prev_row[row_idx+1])
                #     row_idx+=1
                for idx in range(1,row_num):
                    row_val = int((new_row[idx-1]*(row_num+1-idx))/idx)
                    new_row.append(row_val)
                new_row.append(1)
                row_list.append(new_row)
                
        return row_list
        
if __name__=="__main__":
    solution = Solution()
    n= 5
    print(solution.generate(5))
    
