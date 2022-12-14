import numpy as np
def main():
    with open("data/day14_data.txt", "r") as f:
        data = f.readlines()

    lists = [row.strip().split(" -> ") for row in data]
    
    cols = [[int(num.split(",")[0]) for num in row] for row in lists]
    rows = [[int(num.split(",")[1]) for num in row] for row in lists]

    col_nums = [int(num.split(",")[0]) for row in lists for num in row]
    row_nums = [int(num.split(",")[1]) for row in lists for num in row]
    
    col_len = max(col_nums) - min(col_nums) + 1
    
    grid = np.zeros((max(row_nums)+1, col_len)) # Add padding for sand go there
    
    start_col = min(col_nums)

    for row, col in zip(rows, cols):
        row_idx, col_idx = -1, -1
        for r, c in zip(row, col):
            if row_idx == -1:
                row_idx, col_idx = r,c
                continue
            if col_idx == c:
                inc = 1 if r - row_idx > 0 else -1
                idx_c = col_idx - start_col 
                grid[row_idx:r+inc:inc, idx_c] = 1
            else:
                inc = 1 if c - col_idx > 0 else -1
                s_col = col_idx - start_col
                e_col = c - start_col
                grid[row_idx, s_col:(e_col+inc if e_col else None):inc] = 1    # Hack for including 0 index backwards slicing

            row_idx, col_idx = r,c
    
    grid = np.vstack((grid, np.zeros(col_len)))
    grid = np.vstack((grid, np.ones(col_len)))
    
    source_col = 500
    col = source_col - start_col
    row = 0
    row_size, col_size = np.shape(grid)
    row_size -= 1
    col_size -= 1
    silver, silver_flag = 0, False
    sand_units = 0
    while True:
        if not silver_flag and row == row_size-1:
            silver = sand_units
            silver_flag = True
        
        if col_size == col+1:
            grid = np.hstack((grid, np.zeros((np.shape(grid)[0],1))))
            grid[-1, -1] = 1
            col_size += 1
        elif col-1 == 0:
            grid = np.hstack((np.zeros((np.shape(grid)[0],1)), grid))
            grid[row_size, 0] = 1
            col_size += 1
            start_col -= 1

        if not grid[row+1, col]:
            row += 1
            continue
        elif not grid[row+1, col-1]:
            row += 1
            col -= 1
            continue
        elif not grid[row+1, col+1]:
            row += 1 
            col += 1
            continue
        else:
            grid[row, col] = 1
            sand_units += 1
            if row == 0 and col == 500 - start_col:
                break
            col = 500 - start_col
            row = 0

    print(f'Silver: {silver}')
    print(f'Gold: {sand_units}')

    
if __name__ == "__main__":
    main()