from math import prod 
def main():

    with open("day8_data.txt", "r") as f:
        data = f.readlines()

    c_size = len(data)
    r_size = len(data[0].strip())

    visable_trees = 0
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

    scenic_score = 0
    for row in range(c_size):
        for column in range(r_size):
            marker_tree = int(data[row][column])
            tree_distances = []

            distance = 0
            for i in reversed(range(0,row)):
                distance += 1
                target_tree = int(data[i][column])
                if target_tree >= marker_tree:
                    break
            tree_distances.append(distance)
            
            distance = 0
            for i in range(row+1,c_size):
                distance += 1
                target_tree = int(data[i][column])
                if target_tree >= marker_tree:
                    break
            tree_distances.append(distance)

            distance = 0
            for j in reversed(range(0,column)):
                distance += 1
                target_tree = int(data[row][j])
                if target_tree >= marker_tree:
                    break
            tree_distances.append(distance)

            
            distance = 0
            for j in range(column+1,r_size):
                distance += 1
                target_tree = int(data[row][j])
                if target_tree >= marker_tree:
                    break
            tree_distances.append(distance)

            
            tree_score = prod(tree_distances)
            scenic_score = tree_score if tree_score > scenic_score else scenic_score
    
    print(scenic_score)
            
            

            

    
if __name__ == "__main__":
    main()