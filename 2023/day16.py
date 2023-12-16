from utilities.get_data import get_data
from enum import Enum
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    max_row_idx = len(data) - 1
    max_col_idx = len(data[0]) - 1

    class Direction(Enum):
        RIGHT = (0,1)
        LEFT = (0,-1)
        UP = (-1, 0)
        DOWN = (1, 0)

    def energized_tiles(starting_row, starting_col, starting_dir):
        energized = set()
        positions =[[starting_row, starting_col, starting_dir]]

        while positions:
            row, col, direction = positions.pop()
            
            current_row = row + direction.value[0]
            current_col = col + direction.value[1]
            # Boundaries check
            if current_row < 0 or current_row > max_row_idx or \
               current_col < 0 or current_col > max_col_idx:
                continue
                
            tile = data[current_row][current_col]
            if tile == '.' or (tile == '-' and direction in [Direction.RIGHT, Direction.LEFT]) \
                           or (tile == '|' and direction in [Direction.UP, Direction.DOWN]):
                new_direction = [direction]
            elif tile == '-':
                new_direction = [Direction.RIGHT, Direction.LEFT]
            elif tile == '|':
                new_direction = [Direction.UP, Direction.DOWN]
            else:   # Case \ or /
                match(direction):
                    case Direction.RIGHT:
                        new_direction = [Direction.UP]
                    case Direction.LEFT:
                        new_direction = [Direction.DOWN]
                    case Direction.UP:
                        new_direction = [Direction.RIGHT]
                    case Direction.DOWN:
                        new_direction = [Direction.LEFT]
                if tile == '\\':
                    # If the mirror is the opposite, chance direction to opposite
                    new_direction = Direction((new_direction[0].value[0] *-1, new_direction[0].value[1] *-1))
                    new_direction = [new_direction]

            for direc in new_direction:
                if (current_row, current_col, direc) not in energized:
                    positions.append((current_row, current_col, direc))
                    energized.add((current_row, current_col, direc))
        
        unique_positions = set([(row, col) for row, col, direction in energized])
        return len(unique_positions)

    if mode == 'silver':
        mode_total = energized_tiles(0,-1,Direction.RIGHT)
    else:
        totals = []
        # North and South Bound
        for i in range(0, max_col_idx):
            total_north = energized_tiles(-1, i, Direction.DOWN)
            total_south = energized_tiles(max_row_idx+1, i, Direction.UP)
            totals.append(total_north)
            totals.append(total_south)
        # West and East Bound
        for i in range(0, max_row_idx):
            total_west = energized_tiles(i,-1, Direction.RIGHT)
            total_east = energized_tiles(i, max_col_idx+1, Direction.LEFT)
            totals.append(total_west)
            totals.append(total_east)

        mode_total = max(totals)

    print(f'{mode} : {mode_total}')

if __name__ == "__main__":
    main()
    main('gold')