import sys
from time import sleep
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, GRID, Coordinate
from utilities.test_framework import testable
from utilities.helper_funs import nums
import re
from math import prod
# @testable(__file__, (12, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    if data_type.startswith('test'):
        max_x, max_y = 11, 7
    else:
        max_x, max_y = 101, 103

    quadrants = [0, 0, 0, 0] # TopLeft, TopRight, DownLeft, DownRight
    Grid = GRID(max_x, max_y, loopover=True)
    current_positions: list[Coordinate] = []
    velocities: list[Coordinate] = []
    for line in data:
        robot = nums(re.findall(r'-?\d+', line))
        current_positions.append(Coordinate(robot[0], robot[1]))
        velocities.append(Coordinate(robot[2], robot[3]))

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

    def print_to_screen(locations: list[Coordinate], max_x: int, max_y: int):
        print_string = [['.' for _ in range(max_x)] for _ in range(max_y)]
        for pos in locations:
            print_string[pos.y][pos.x] = "#"
        print_string = "\n".join(["".join(s) for s in print_string])

        with open("data/day14_screen.txt",'w') as f:
            f.write(print_string)

    silver = prod(quadrants)
    print(f'{silver = }')


    inc = 1 # Use this to jump ahead and iterate the position until you can use just input
    speed = 0.2
    if data_type != 'test':
        i = -1 + inc
        for k, (pos, vel) in enumerate(zip(current_positions, velocities)):
            Grid.current_point = pos
            Grid.move(vel *inc)
            current_positions[k] = Grid.current_point


        while (i := i + 1) <= 1e7:
            for k, (pos, vel) in enumerate(zip(current_positions, velocities)):
                Grid.current_point = pos
                Grid.move(vel)
                current_positions[k] = Grid.current_point

            print_to_screen(current_positions, max_x, max_y)
            sleep(speed)
            # input() # Uncomment this when we are close
            print(i)

    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")