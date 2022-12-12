import numpy as np
def main():
    with open("data/day12_data.txt", "r") as f:
        data = f.readlines()
    
    # Let's make numpy matrix from the string data
    data = np.array([list(line.strip()) for line in data])

    # First find the start and end points
    start_pos = np.where(data == 'S')
    end_pos = np.where(data == "E")

    # Replace with 'correct letters'
    data[start_pos] = "a"
    data[end_pos] = "z"

    # Search algorithm was orginally wikipedia A* psedo-code implementation
    # After stripping this down, this has no heuristic function, so basically
    # some kind of uniform-search algorithm
    def A_star(s,e, matrix, part):
        open_set = [s]
        row_size, col_size = np.shape(matrix)

        # This keeps track of distance to each node
        g_scores = np.full(np.shape(matrix), np.inf)
        g_scores[s] = 0

        while open_set:
            current = open_set[0]

            if part == 1 and current == e:
                return g_scores[current]
            elif part == 2 and matrix[current][0] == e:
                return g_scores[current]
            
            open_set.remove(current)
            neighbors = []
            if current[1] != col_size -1:
                neighbors.append((current[0], current[1]+1))
            if current[1] != 0:
                neighbors.append((current[0], current[1]-1))
            if current[0] != row_size -1:
                neighbors.append((current[0]+1, current[1]))
            if current[0] != 0:
                neighbors.append((current[0]-1, current[1]))

            for neighbor in neighbors:
                tentative_g_score = g_scores[current]
                if part == 1:
                    tentative_g_score += 1 if ord(matrix[neighbor][0]) - ord(matrix[current][0]) <= 1 else np.inf
                else:
                    tentative_g_score += 1 if ord(matrix[current][0]) - ord(matrix[neighbor][0]) <= 1 else np.inf
                
                if tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    if neighbor not in open_set:
                        open_set.append(neighbor)
        
        print("FAILED!")
        return

    silver = A_star(start_pos, end_pos, data, part=1)
    gold = A_star(end_pos, "a", data, part=2)
    print(f"Silver: {int(silver)}")
    print(f"Gold: {int(gold)}")

if __name__ == "__main__":
    main()