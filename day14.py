import numpy as np
def main():
    with open("data/day14_test_data.txt", "r") as f:
        data = f.readlines()

    lists = [row.strip().split(" -> ") for row in data]
    cols = [int(num.split(",")[0]) for row in lists for num in row]
    rows = [int(num.split(",")[1]) for row in lists for num in row]
    
    start_col = min(cols)
    col_len = max(cols) - start_col + 1
    
    grid = np.zeros((max(rows)+1, col_len))
    
    # Fill empty grid with 1 if there is wall
    row_idx, col_idx = -1, -1
    for row, col in zip(rows, cols): 
        if col_idx == col:
            inc = 1 if row - row_idx > 0 else -1
            s_col = col_idx - start_col
            grid[row_idx:row+inc:inc, s_col] = 1
        elif row_idx == row:
            inc = 1 if col - col_idx > 0 else -1
            s_col = col_idx - start_col
            tmp = col - start_col
            e_col = (tmp+inc if tmp else None)  # Hack for including 0 index backwards slicing
            grid[row_idx, s_col:e_col:inc] = 1
        
        row_idx, col_idx = row, col

    # Two rows below: one empty and one floor
    grid = np.vstack((grid, np.zeros(col_len)))
    grid = np.vstack((grid, np.ones(col_len)))
    
    row_size = np.shape(grid)[0] - 1
    col_size = np.shape(grid)[1] - 1

    silver, silver_flag = 0, False
    sand_units = 0
    source_col = 500 - start_col
    col = source_col
    row = 0
    while True:
        if not silver_flag and row == row_size-1:
            silver = sand_units
            silver_flag = True
        
        # add columns to grid if close border 
        if col+1 == col_size:
            grid = np.hstack((grid, np.zeros((np.shape(grid)[0],1))))
            grid[-1, -1] = 1
            col_size += 1
        elif col-1 == 0:
            grid = np.hstack((np.zeros((np.shape(grid)[0],1)), grid))
            grid[row_size, 0] = 1
            col_size += 1
            source_col += 1

        if not grid[row+1, col]:
            row += 1
        elif not grid[row+1, col-1]:
            row += 1
            col -= 1
        elif not grid[row+1, col+1]:
            row += 1 
            col += 1
        else:
            grid[row, col] = 1
            sand_units += 1
            if row == 0 and col == source_col:
                break
            col = source_col
            row = 0

    print(f'Silver: {silver}')
    print(f'Gold: {sand_units}')

    
if __name__ == "__main__":
    main()