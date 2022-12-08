from time import perf_counter
def main():
    with open("od1i.txt/bigboy.txt", "r") as f:
        data = f.readlines()

    c_size = len(data)
    r_size = len(data[0].strip())

    seen_trees = []

    def find_trees(line, idx, vertical, backwards):
        length = len(line)
        line = reversed(line) if backwards else line

        largest_tree = -1
        for x, tree in enumerate(line):
            tree = int(tree)
            if largest_tree < int(tree):
                x = length - (x+1) if backwards else x
                largest_tree = tree
                seen_trees.append((idx,x) if vertical else (x,idx))

    # Go through all the data rows
    for i,row in enumerate(data):
        row = row.strip()
        find_trees(row, i, False, False)
        find_trees(row, i, False, True)

    # Go through all the data column
    for j in range(r_size):
        column = ""
        for i in range(c_size):
            column += data[i][j]
        find_trees(column,j, True, False)
        find_trees(column,j, True, True)

    # Remove repeated 
    unique_trees = list(set(seen_trees))
    print(len(unique_trees))

    # Part 2

    # We use VERY generalized function to loop from given starting point
    def tree_distance_counter(row, column, direction):
        backwards = direction in ['N', 'W']
        vertical = direction in ['N', 'S']
        fixed_idx = column if vertical else row
        marker_tree = int(data[row][column])
        
        s = (row if vertical else column) + (-1 if backwards else 1)
        e = -1 if backwards else c_size if vertical else r_size
        inc = -1 if backwards else 1
        
        distance = 0
        for x in range(s,e,inc):
            distance += 1
            target_tree = data[x][fixed_idx] if vertical else data[fixed_idx][x]
            if int(target_tree) >= marker_tree: 
                break
        return distance

    # Actual solution to part 2
    scenic_score = 0
    for row in range(c_size):
        for column in range(r_size):
            # Labeling idea from Eetu Knutars turned into better generalized function
            dist1 = tree_distance_counter(row, column, "N") # North
            dist2 = tree_distance_counter(row, column, "E") # East
            dist3 = tree_distance_counter(row, column, "S") # South
            dist4 = tree_distance_counter(row, column, "W") # West

            tree_score = dist1*dist2*dist3*dist4
            scenic_score = tree_score if tree_score > scenic_score else scenic_score
    
    print(scenic_score)

if __name__ == "__main__":
    s = perf_counter()
    main()
    e = perf_counter()
    print(f'Time {e-s:.2f} (s)')