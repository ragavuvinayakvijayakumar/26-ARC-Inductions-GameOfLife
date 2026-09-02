def count_neighbors(grid, row, col):
    len_column,len_row  = len(grid[0]),len(grid)
    min_row,min_column  = max(row-1,0), max(col-1,0)
    max_row,max_column= min(row+1,len_row-1),min(col+1,len_column-1)
    alive_count = 0
    for i in range(min_row,max_row+1):
        for j in range(min_column,max_column+1):
            alive_count += grid[i][j]
    alive_count -= grid[row][col]
    return alive_count 
    
def compute_next_generation(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0,rows):
        for j in range(0,cols):
            alive_count = count_neighbors(grid,i,j)
            if grid[i][j] == 1:
                if alive_count <2:
                    next_grid[i][j] = 0
                if 1< alive_count < 4 :
                    next_grid[i][j] = 1
                if 3< alive_count:
                    next_grid[i][j] = 0
            else:
                if alive_count == 3 :
                    next_grid[i][j] = 1
                    
    return next_grid
