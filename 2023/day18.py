from utilities.get_data import get_data
import re
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    direction_step = {
        'R' : (0, 1),
        'L' : (0,-1),
        'U' : (-1, 0),
        'D' : (1, 0)
    }

    current_node = (0,0)
    border = set([current_node])
    for line in data:
        direction, dig_out = re.match(r'(R|D|L|U) (\d+)', line).groups()
        increment = direction_step[direction]
        
        for i in range(int(dig_out)):
            current_node = (current_node[0] + increment[0], current_node[1] + increment[1])
            border.add(current_node)

    deepest_row = max([x[0] for x in border])
    widest_col = max([x[1] for x in border])
    col_offset = min([x[1] for x in border])
    row_offset = min([x[0] for x in border])

    all_stats = [['.' for j in range(widest_col+1-col_offset)] for i in range(-row_offset+ deepest_row+1)]
    for node in border:
        all_stats[node[0]-row_offset][node[1] -col_offset] = '#'
    
    all_stats = ["".join(line) for line in all_stats]

    with open('tmp.txt', 'w') as f:
        for stat in all_stats:
            f.write(stat + "\n")

    # Find a point that is for certain to be inside
    first_dot = None
    for row in range(row_offset, deepest_row+1):
        tmp_list = list(filter(lambda x:x[0] == row, border))
        tmp_cols = [x[1] for x in tmp_list]
        tmp_cols.sort()

        first = tmp_cols[0]
        second = tmp_cols[1]
        if second - first == 1:
            continue
        first_dot = (row, first+1)
        break

    assert first_dot is not None, 'Ei menny hyvin!'
    
    # Count by spreding to neigbouring dots
    queue = [first_dot]
    visited = set()
    total = 0
    while queue:
        current_dot = queue.pop(0)
        for direction in ['R', 'L', 'U', 'D']:
            step = direction_step[direction]
            next_dot = (current_dot[0] + step[0], current_dot[1] + step[1])
            if next_dot not in border and next_dot not in visited:
                total += 1
                queue.append(next_dot)
                visited.add(next_dot)
    total += len(border)

    print(f'{mode} : {total}')

if __name__ == "__main__":
    print('test: ', end='')
    main(data_type='test2')
    main()