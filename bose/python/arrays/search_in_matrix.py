def searchMatrix(matrix,target):
        
    # for i in range(0,len(matrix)):
    #     if target >= matrix[i][0] and target <= matrix[i][len(matrix[0])-1]:
    #         for j in range(0,len(matrix[0])):
    #             print("Matrix value at i={} and j={} is {}".format(i,j,matrix[i][j]))
    #             if matrix[i][j]==target:
    #                 return True
    #             j+=1
    #     else:
    #         i+=1
    # return False

    n = len(matrix)
    m = len(matrix[0])

    i=0
    j = m-1

    while i<n and j>=0:
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            j-=1
        else:
            i+=1
    return False

if __name__ == "__main__":
    x= [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(searchMatrix(x,70))