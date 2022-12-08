def main():

    with open("day8_data.txt", "r") as f:
        data = f.readlines()

    c_size = len(data)
    r_size = len(data[0].strip())

    seen_trees = []

    for i,row in enumerate(data):
        row = row.strip()
        largest_tree = -1
        for j,tree in enumerate(row):
            tree = int(tree)
            if largest_tree < int(tree):
                largest_tree = tree
                seen_trees.append((i,j))

        largest_tree = -1
        for j,tree in enumerate(reversed(row)):
            j = r_size - j -1
            tree = int(tree)
            if largest_tree < int(tree):
                largest_tree = tree
                seen_trees.append((i,j))

    for j in range(r_size):
        column = ""
        for i in range(c_size):
            column += data[i][j]
        
        largest_tree = -1
        for i,tree in enumerate(column):
            tree = int(tree)
            if largest_tree < int(tree):
                largest_tree = tree
                seen_trees.append((i,j))

        largest_tree = -1
        for i,tree in enumerate(reversed(column)):
            i = c_size - i -1
            tree = int(tree)
            if largest_tree < int(tree):
                largest_tree = tree
                seen_trees.append((i,j))

    

    unique_trees = list(set(seen_trees))
    print(len(unique_trees))
    print(len(seen_trees))

    def tree_distance_counter(marker_tree, check_range, ref_idx, row=True):
        distance = 0
        for x in check_range:
            distance += 1
            target_tree = int(data[ref_idx][x]) if row else int(data[x][ref_idx])
            if target_tree >= marker_tree:
                break
        return distance

    scenic_score = 0
    for row in range(c_size):
        for column in range(r_size):
            marker_tree = int(data[row][column])

            range1 = reversed(range(column))
            range2 = range(column+1,r_size)
            range3 = reversed(range(row))
            range4 = range(row+1,c_size)

            # Labeling idea from Eetu Knutas
            dist1 = tree_distance_counter(marker_tree, range1, row, True) # West
            dist2 = tree_distance_counter(marker_tree, range2, row, True) # East
            dist3 = tree_distance_counter(marker_tree, range3, column, False) # North
            dist4 = tree_distance_counter(marker_tree, range4, column, False) # South

            tree_score = dist1*dist2*dist3*dist4
            scenic_score = tree_score if tree_score > scenic_score else scenic_score
    
    print(scenic_score)

if __name__ == "__main__":
    main()