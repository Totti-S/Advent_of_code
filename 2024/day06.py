import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import test
from collections.abc import Iterator

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    max_coord = len(data)
    guard = ['^', '>', 'v', '<']
    dirs = dict(zip(guard, [Coordinate.UP, Coordinate.RIGHT, Coordinate.DOWN, Coordinate.LEFT]))
    rotate = dict(zip(dirs.values(), [Coordinate.RIGHT, Coordinate.DOWN, Coordinate.LEFT, Coordinate.UP]))

    # Find the starting spot
    for start_y, line in enumerate(data):
        if any(pos :=[g in line for g in guard]):
            symbol = guard[pos.index(True)]
            start_x = line.index(symbol)
            starting_dir = dirs[symbol]
            break
    # Make a proper grid
    data = [[char for char in line] for line in data]

    starting_pos = Coordinate(start_x, start_y)
    positions = set([starting_pos])
    dir_and_pos = set([(starting_pos, starting_dir)])
    
    def move_guard(pos: Coordinate, direc: Coordinate) -> Iterator[tuple[Coordinate, Coordinate]]:
        while True:
            next_p = pos + direc
            if next_p.y in [-1, max_coord] or next_p.x in [-1, max_coord]:
                break
            elif data[next_p.y][next_p.x] == '#':
                direc = rotate[direc]
            else:
                pos = next_p
            yield pos, direc

    tested_obstructions: set[Coordinate] = set()
    pos, direc = starting_pos, starting_dir
    for new_pos, new_dir in move_guard(starting_pos, starting_dir):
        positions.add(new_pos)
        if pos != new_pos and new_pos not in tested_obstructions:
            # Modify this data for moment to find out if this generates a loop
            data[new_pos.y][new_pos.x] = '#'
            test_set = dir_and_pos.copy()
            for pos_dir in move_guard(pos, direc):
                if pos_dir in test_set: # loop decetion
                    gold +=1
                    break
                test_set.add(pos_dir)
            tested_obstructions.add(new_pos)
            data[new_pos.y][new_pos.x] = '.'
        dir_and_pos.add((new_pos, new_dir))
        pos, direc = new_pos, new_dir
    silver = len(positions)

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")
    test(main, __file__, (41, 6), (None, 1), (None, 1), (None, 1))