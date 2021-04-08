def numIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0 #no islands because grid is empty
    cols = len(grid[0])


    num_islands =0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=="1":
                num_islands += 1
                markCurrentIsland(grid,i,j,rows,cols)
    
    return num_islands


def markCurrentIsland(grid,i,j,rows,cols):
    if (i<0) or (i>=rows) or (j<0) or (j>=cols) or (grid[i][j]!="1"):
        return 
    grid[i][j] =2
    markCurrentIsland(grid,i+1,j,rows,cols)
    markCurrentIsland(grid,i,j+1,rows,cols)
    markCurrentIsland(grid,i-1,j,rows,cols)
    markCurrentIsland(grid,i,j-1,rows,cols)


if __name__ == "__main__":
    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    #     ]
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    print("Number islands are :: {}".format(numIslands(grid)))