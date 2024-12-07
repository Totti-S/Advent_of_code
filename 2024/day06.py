import sys
sys.path.append('..')
import utilities.directions as DIRS
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import test
from collections.abc import Iterator

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    max_coord = len(data)

    # Find the starting spot
    for start_y, line in enumerate(data):
        if (start_x := line.find('^') ) != -1:
            break

    # Make a proper grid
    data = [[char for char in line] for line in data]

    starting_pos = Coordinate(start_x, start_y)
    starting_dir = DIRS.UP
    positions = set([starting_pos])
    dir_and_pos = set([(starting_pos, DIRS.UP)])

    def move_guard(pos: Coordinate, direc: Coordinate) -> Iterator[tuple[Coordinate, Coordinate]]:
        while True:
            next_p = pos + direc
            if next_p.y in [-1, max_coord] or next_p.x in [-1, max_coord]:
                break
            elif data[next_p.y][next_p.x] == '#':
                direc = direc.rotate90(clockwise=True)
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