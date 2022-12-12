import numpy as np
def main():
    with open("data/day12_data.txt", "r") as f:
        data = f.readlines()

    a_ord = ord('a')
    data_matrix = []
    start_pos,end_pos = 0,0
    for i,line in enumerate(data):
        line = line.strip()
        numbers = []
        for j,char in enumerate(line):
            if char == "S":
                start_pos = (i,j)
                numbers.append(0)
            elif char == "E":
                end_pos = (i,j)
                numbers.append(ord('z')-ord('a'))
            else:
                numbers.append(ord(char)-ord('a'))
        data_matrix.append(numbers)

    # calculates distabce to endpoint
    def h(node, endNode):
        return np.sqrt(np.square(abs(node[0]-endNode[0])) + np.square(abs(node[1]-endNode[1])))


    def distance(start_node, end_node, matrix):
        a_value = matrix[start_node[0]][start_node[1]]
        b_value = matrix[end_node[0]][end_node[1]]
        if a_value - b_value <= 1:
            return 1
        else:
            return np.inf

    def reconstruct_path(came_from, current):
        total_path = [current]
        while current[0] != -1 or current[1] != -1:
            current = came_from[current[0]][current[1]]
            total_path.append(current)
        return total_path

    def A_star(s,e, matrix):
        open_set = [s]
        row_size, col_size = np.shape(matrix)

        value = np.empty((), dtype=object)
        value[()] = (-1, -1)
        came_from = np.full(np.shape(matrix),value, dtype=object)
        
        g_scores = np.full(np.shape(matrix), np.inf)
        g_scores[s[0]][s[1]] = 0

        f_scores = np.full(np.shape(matrix), np.inf)
        #f_scores[s[0]][s[1]] = h(s,e)

        while open_set:
            lowest_f = np.inf
            current = (0,0)
            for node in open_set:
                if f_scores[node[0]][node[1]] < lowest_f:
                    lowest_f = f_scores[node[0]][node[1]]
                    current = node

            current = open_set[0]

            if matrix[current[0]][current[1]] == 0:
                return reconstruct_path(came_from, current)
            
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
                tentative_g_score = g_scores[current[0]][current[1]] + distance(current, neighbor,matrix)
                if tentative_g_score < g_scores[neighbor[0]][neighbor[1]]:
                    came_from[neighbor[0]][neighbor[1]] = current
                    g_scores[neighbor[0]][neighbor[1]] = tentative_g_score
                    #f_scores[neighbor[0]][neighbor[1]] = tentative_g_score + h(neighbor, e)
                    if neighbor not in open_set:
                        open_set.append(neighbor)
        
        print("FAILED!")
        return


    # path = A_star(start_pos, end_pos, data_matrix)
    # print(path)
    # print(len(path)-2)

    path2 = A_star(end_pos,(0,1),data_matrix)
    print(path2)
    print(len(path2)-2)


if __name__ == "__main__":
    main()