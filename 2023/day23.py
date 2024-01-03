import queue
from utilities.get_data import get_data
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    max_x, max_y = len(data[0]), len(data) 
    directions = dict(zip('RLUD', [(0, 1), (0, -1), (-1, 0), (1, 0)]))
    downhill = dict(zip('RLUD', ['>', '<', '^', 'v']))

    starting_point = (0,1)
    end_point = (max_y-1, data[-1].index('.'))
    
    cross_roads = defaultdict(lambda: defaultdict(int))
    visited = set()

    path = set([starting_point])
    current_node = last_cross_roads = starting_point
    new_paths = []
    both_ways = True
    while True:
        possible_new_paths = []
        for letter, direction in directions.items():
            new_y = current_node[0] + direction[0]
            new_x = current_node[1] + direction[1]
            if not (0 <= new_x < max_x and 0 <= new_y < max_y):
                continue
            symbol = data[new_y][new_x]
            new_position = (new_y, new_x)
            if new_position in path:
                continue
            if symbol == '.':
                possible_new_paths.append(new_position)
            elif symbol == '#':
                continue
            else:
                if symbol == downhill[letter]:
                    both_ways = False
                    possible_new_paths.append(new_position)
        
        if len(possible_new_paths) == 1:
            current_node = possible_new_paths[0]
            path.add(current_node)
            continue
        elif len(possible_new_paths) >= 1: # Found crossroads: This is a new 'node'
            if cross_roads[last_cross_roads][current_node] < len(path):
                cross_roads[last_cross_roads][current_node] = len(path)-1
            
            if both_ways:
                if cross_roads[current_node][last_cross_roads] < len(path):
                    cross_roads[current_node][last_cross_roads] = len(path)-1
            
            for new_node in possible_new_paths:
                pair = (new_node, (current_node, new_node))
                if pair not in visited:
                    new_paths.append(pair)
                    visited.add(pair)
        elif current_node == end_point:
            if cross_roads[last_cross_roads][end_point] < len(path):
                cross_roads[last_cross_roads][end_point] = len(path)-1
        
        if not new_paths:
            break
        current_node, path = new_paths.pop(0)
        last_cross_roads = path[0]
        path = set(list(path))
        both_ways = True
    


    dist = defaultdict(int)
    paths = defaultdict(list)
    djikstra_visited = set()
    current_node = starting_point
    current_dist = 0
    current_path = []
    for node in cross_roads:
        current_dist = dist[node]
        current_path = paths[node] 

        djikstra_visited.add(current_node)
        for n, val in cross_roads[node].items():
            if n not in djikstra_visited:
                if dist[n] < current_dist + val:
                    dist[n] = val + current_dist
                    paths[n] = [*current_path, n]
                
    silver = dist[end_point]
    # print(dist)
    print(f'{mode} : {silver}')


###### GOLD Solution
    
    cross_roads = defaultdict(lambda: defaultdict(int))
    visited = set()

    path = set([starting_point])
    current_node = last_cross_roads = starting_point
    new_paths = []
    while True:
        possible_new_paths = []
        for letter, direction in directions.items():
            new_y = current_node[0] + direction[0]
            new_x = current_node[1] + direction[1]
            if not (0 <= new_x < max_x and 0 <= new_y < max_y):
                continue
            symbol = data[new_y][new_x]
            new_position = (new_y, new_x)
            if new_position in path:
                continue
            if symbol == '.':
                possible_new_paths.append(new_position)
            elif symbol == '#':
                continue
            else:
                possible_new_paths.append(new_position)
        
        if len(possible_new_paths) == 1:
            current_node = possible_new_paths[0]
            path.add(current_node)
            continue
        elif len(possible_new_paths) >= 1: # Found crossroads: This is a new 'node'
            if cross_roads[last_cross_roads][current_node] < len(path):
                cross_roads[last_cross_roads][current_node] = len(path)-1
            
            if cross_roads[current_node][last_cross_roads] < len(path):
                cross_roads[current_node][last_cross_roads] = len(path)-1
            
            for new_node in possible_new_paths:
                pair = (new_node, (current_node, new_node))
                if pair not in visited:
                    new_paths.append(pair)
                    visited.add(pair)

        elif current_node == end_point:
            if cross_roads[last_cross_roads][end_point] < len(path):
                cross_roads[last_cross_roads][end_point] = len(path)-1
        
        if not new_paths:
            break
        current_node, path = new_paths.pop(0)
        last_cross_roads = path[0]
        path = set(list(path))
    

    dist = defaultdict(int)
    paths = defaultdict(list)
    djikstra_visited = set()
    current_dist = 0
    current_path = []

    def rec(node, current_dist, current_path):
        for n, val in cross_roads[node].items():
            if n in current_path: continue
            if dist[n] < current_dist + val:
                dist[n] = current_dist + val
            if n != end_point:
                tmp_path = [*current_path, n]
                tmp_dist = current_dist + val
                rec(n, tmp_dist, tmp_path)

    rec(starting_point, current_dist, current_path)
    gold = dist[end_point]
    # print(cross_roads)
    # print(paths[end_point])
    print(f'Gold : {gold}')



if __name__ == "__main__":
    main()