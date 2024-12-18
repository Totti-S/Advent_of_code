from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
from utilities.helper_funs import nums
import utilities.directions as dirs

@testable(__file__, (36, 81), (3, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    data = [nums([char for char in line]) for line in data]
    max_x, max_y = len(data[0]), len(data)

    start_point_coords: set[Coordinate] = set()
    start_point_coords.update(
        Coordinate(x, y)
        for y, line in enumerate(data)
        for x, num in enumerate(line)
        if num == 0
    )

    # Put everything in prio que to be checked
    current_stack: dict[Coordinate, int] = defaultdict(int)
    next_stack: dict[Coordinate, int] = defaultdict(int)

    for start in start_point_coords:
        current_stack = defaultdict(int)
        current_stack[start] += 1
        for next_val in range(1, 10):
            for node, weight in current_stack.items():
                for coord in dirs.adj4(node):
                    if coord.x in [-1, max_x] or coord.y in [-1, max_y]:
                        continue
                    if data[coord.y][coord.x] == next_val:
                        next_stack[coord] += weight
            current_stack = next_stack.copy()
            next_stack.clear()
        silver += len(current_stack)
        gold += sum(current_stack.values())

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")