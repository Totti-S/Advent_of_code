from utilities.get_data import get_data
from enum import Enum
import re
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=True)
    max_rows = len(data)
    max_cols = len(data[0])

    def count_turns(path, turn):
        return len(path)-len(path.rstrip(turn))
    
    direction = {
        'R' : (0, 1),
        'L' : (0,-1),
        'U' : (-1, 0),
        'D' : (1, 0)
    }

    opposite_direction = {
        'R' : 'L',
        'L' : 'R',
        'U' : 'D',
        'D' : 'U'
    }

    end_row, end_col = max_rows - 1, max_cols -1   # Down right corner is end point
    end_node = (end_row, end_col)

    # Need to make the first iteration outside of the loop (for now)
    queue = [(0, 1, 'R'), (1, 0, 'D')] 
    memory = {
        (0, 1) : {'R' : data[0][1]},
        (1, 0) : {'D' : data[1][0]},
    }
    def memory_check(node, turn, count):
        row, col, path = node
        add_row, add_col = direction[turn]
        next_node = (row+add_row, col+add_col)
        if 0 <= next_node[0] < max_rows and 0 <= next_node[1] < max_cols:
            next_path = (count+1) * turn
            path_len = memory[(row,col)][path] + data[next_node[0]][next_node[1]]
            
            if next_node != end_node and end_node in memory and path_len > min(memory[end_node].values()):
                return
            if next_node not in memory or next_path not in memory[next_node] or path_len < memory[next_node][next_path]:
                if next_node not in memory:
                    memory[next_node] = {}
                memory[next_node][next_path] = path_len
                queue.append((*next_node, next_path))

    if mode == 'silver':
        while queue:
            node = queue.pop(0)
            _,_, path = node
            
            for turn in ['L', 'R', 'U', 'D']:
                if path[-1] != opposite_direction[turn] and (count := count_turns(path, turn)) < 3:
                    memory_check(node, turn, count)

    else:
        while queue:
            node = queue.pop(0)
            row, col, path = node
            turn = path[-1]
            if (count := count_turns(path, turn)) < 4:
                add_row, add_col = direction[turn]
                next_node = (row+add_row, col+add_col)
                if turn == 'R' and next_node[1] == max_cols - 1 and count < 3:
                    continue
                if turn == 'L' and next_node[1] == 0 and count < 3:
                    continue
                if turn == 'U' and next_node[0] == 0 and count < 3:
                    continue
                if turn == 'D' and next_node[0] == max_rows - 1 and count < 3:
                    continue
                memory_check(node, turn, count)
            else:
                for t in ['L', 'R', 'U', 'D']:
                    add_row, add_col = direction[t]
                    next_node = (row+add_row, col+add_col)
                    if ((count := count_turns(path, t)) == 10 and t == turn) or path[-1] == opposite_direction[t]: 
                        continue
                    if t == 'R' and next_node[1] == max_cols - 1 and count < 3:
                        continue
                    if t == 'L' and next_node[1] == 0 and count < 3:
                        continue
                    if t == 'U' and next_node[0] == 0 and count < 3:
                        continue
                    if t == 'D' and next_node[0] == max_rows - 1 and count < 3:
                        continue
                    memory_check(node, t, count)

    min_value = 1_000_000
    # min_path = None
    for val in memory[end_node].values():
        if val < min_value:
            min_value = val
            # min_path = path
    
    print(f'{mode} : {min_value}')

if __name__ == "__main__":
    main('gold')