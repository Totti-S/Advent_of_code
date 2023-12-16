from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    max_row_idx = len(data) - 1
    max_col_idx = len(data[0]) - 1
    # print(data)

    direction_travel = {
        'R' : (0,1),
        'L' : (0,-1),
        'U' : (-1,0),
        'D' : (1,0),
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
                    match(direction):
                        case 'R':
                            new_direction = 'U'
                        case 'L':
                            new_direction = 'D'
                        case 'U':
                            new_direction = 'R'
                        case 'D':
                            new_direction = 'L'
                case '\\':
                    match(direction):
                        case 'R':
                            new_direction = 'D'
                        case 'L':
                            new_direction = 'U'
                        case 'U':
                            new_direction = 'L'
                        case 'D':
                            new_direction = 'R'
                case '-':
                    if direction in ['R', 'L']:
                        new_direction = direction
                    else:
                        new_direction = ['R', 'L']
                case '|':
                    if direction in ['U', 'D']:
                        new_direction = direction
                    else:
                        new_direction = ['U', 'D']
                
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
        mode_total = energized_tiles(0,-1,'R')
    else:
        totals = []
        # North and South Bound
        for i in range(0, max_col_idx):
            total_north = energized_tiles(-1, i, 'D')
            total_south = energized_tiles(max_row_idx+1, i, 'U')
            totals.append(total_north)
            totals.append(total_south)
        # West and East Bound
        for i in range(0, max_row_idx):
            total_west = energized_tiles(i,-1,'R')
            total_east = energized_tiles(i, max_col_idx+1, 'L')
            totals.append(total_west)
            totals.append(total_east)

        mode_total = max(totals)

    print(f'{mode} : {mode_total}')

if __name__ == "__main__":
    main()
    main('gold')