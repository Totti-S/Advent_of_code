from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    max_row_idx = len(data) - 1
    max_col_idx = len(data[0]) - 1
    # print(data)

    direction_travel = {
        'right' : (0,1),
        'left' : (0,-1),
        'up' : (-1,0),
        'down' : (1,0),
    }

    def energized_tiles(starting_row, starting_col, starting_dir):
        # NOTE Starting position has to be outside of the grid
        energized = set()
        positions =[[starting_row, starting_col, starting_dir]]

        while positions:
            row, col, direction = positions.pop()
            direction_step = direction_travel[direction]
            
            current_row = row + direction_step[0]
            current_col = col + direction_step[1]
            # Boundaries check
            if direction_step[0] + row < 0 or direction_step[0] + row > max_row_idx:
                continue
            elif direction_step[1] + col < 0 or direction_step[1] + col > max_col_idx:
                continue

            match (data[current_row][current_col]):
                case '.':
                    new_direction = direction
                case '/':
                    if direction == 'right':
                        new_direction = 'up'
                    elif direction == 'left':
                        new_direction = 'down'
                    elif direction == 'up':
                        new_direction = 'right'
                    elif direction == 'down':
                        new_direction = 'left'
                case '\\':
                    if direction == 'right':
                        new_direction = 'down'
                    elif direction == 'left':
                        new_direction = 'up'
                    elif direction == 'up':
                        new_direction = 'left'
                    elif direction == 'down':
                        new_direction = 'right'
                case '-':
                    if direction in ['right', 'left']:
                        new_direction = direction
                    else:
                        new_direction = ['right', 'left']
                case '|':
                    if direction in ['up', 'down']:
                        new_direction = direction
                    else:
                        new_direction = ['up', 'down']
                
            if type(new_direction) is list:
                for direc in new_direction:
                    if (current_row, current_col, direc) not in energized:
                        positions.append((current_row, current_col, direc))
                        energized.add((current_row, current_col, direc))
            else:
                if (current_row, current_col, new_direction) not in energized:
                    positions.append((current_row, current_col, new_direction))
                    energized.add((current_row, current_col, new_direction))
        
        unique_positions = set()
        for val in energized:
            row, col, direction = val
            unique_positions.add((row,col))
        return len(unique_positions)

    if mode == 'silver':
        mode_total = energized_tiles(0,-1,'right')
    else:
        totals = []
        # North Bound
        for i in range(0, max_col_idx):
            total = energized_tiles(-1, i, 'down')
            totals.append(total)
        # West and East Bound
        for i in range(0, max_row_idx):
            total_west = energized_tiles(i,-1,'right')
            total_east = energized_tiles(i, max_col_idx+1, 'left')
            totals.append(total_west)
            totals.append(total_east)

        # South Bound
        for i in range(0, max_col_idx):
            total = energized_tiles(max_row_idx+1, i, 'up')
            totals.append(total)
        mode_total = max(totals)

    print(f'{mode} : {mode_total}')

if __name__ == "__main__":
    main()
    main('gold')