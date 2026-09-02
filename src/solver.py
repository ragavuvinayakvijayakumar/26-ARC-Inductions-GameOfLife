import math 
#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    len_column = len(grid[0])
    len_row = len(grid)
    min_row = max(row-1,0)
    min_column = max(column-1,0) 
    max_row = min(row+1,len_row)
    max_column = min(column+1,len_column)
    alive_count = 0
    for i in range(min_row,max_row+1):
        for j in range(min_column,max_column+1):
            alive_count += grid[j][i]
            j++
        i++
    alive_count -= grid[row][col]
    return alive_count 
    
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(0,rows):
        for j in range(0,cols):
            alive_count = count_neighours(grid,i,j)
            if gird[i][j] = 1:
                if alive_count <2:
                    next_grid[i][j] = 0
                if 1< alive_count < 4 :
                    next_grid[i][j] = 1
                if 3< alive_count:
                    next_grid[i][j] = 0
            else:
                if alive_count =3 :
                    next_grid[i][j] = 1
    return next_grid
