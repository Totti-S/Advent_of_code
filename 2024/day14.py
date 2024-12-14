from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, GRID, Coordinate
from utilities.test_framework import testable
from utilities.helper_funs import nums
import re
from math import prod
@testable(__file__, (12, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    if data_type.startswith('test'):
        max_x, max_y = 11,7
    else:
        max_x, max_y = 101,103

    # memory = defaultdict(int) # Debugging memory

    quadrants = [0, 0, 0, 0] # TopLeft, TopRight, DownLeft, DownRight
    Grid = GRID(max_x, max_y, loopover=True)
    for line in data:
        robot = nums(re.findall(r'-?\d+', line))

        Grid.current_point = Coordinate(robot[0], robot[1])
        after_100s = Coordinate(robot[2], robot[3]) * 100
        Grid.move(after_100s)

        index = 0
        # memory[(Grid.current_point.x,Grid.current_point.y)] += 1
        if Grid.current_point.y == (max_y // 2) or Grid.current_point.x == (max_x // 2):
            continue
        if max_y // 2 <= Grid.current_point.y:
            index += 2
        if max_x // 2 <= Grid.current_point.x:
            index += 1
        quadrants[index] += 1

    # print()
    # for i in range(max_y):
    #     for j in range(max_x):
    #         if (j, i) in memory:
    #             print(memory[(j,i)], end="")
    #         else:
    #             print(".", end="")
    #     print()
    # print()

    silver = prod(quadrants)
    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")