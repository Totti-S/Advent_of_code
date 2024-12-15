import sys
from time import sleep
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
import utilities.directions as Dirs  

@testable(__file__, (10092, 9021))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False, has_portions=True)
    silver, gold = 0, 0

    # Find the robot
    for start_y, line in enumerate(data[0]):
        if (start_x := line.find('@') ) != -1:
            break

    current_postition = Coordinate(start_x, start_y)
    
    grid: list[list[str]] = [[c for c in line] for line in data[0]]
    commands: str = "".join(data[1])

    movement = {
        "^": Dirs.UP,
        "v": Dirs.DOWN,
        "<": Dirs.LEFT,
        ">": Dirs.RIGHT,
    }

    def print_current_arrangement(grid, robot = None, movement= None):
        sleep(0.35)
        print(robot, movement)
        print()
        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if (x, y) != robot:
                    print(char, end="")
                else:
                    print("@", end="")
            print()
        print()

    # print_current_arrangement()

    grid[start_y][start_x] = "."
    for command in commands:
        direction = movement[command]
        next_pos = current_postition + direction
        symbol = grid[next_pos.y][next_pos.x]
        if symbol == "#":
            continue
        elif symbol == "O":
            box_moving_allowed = False
            i = 1
            box = next_pos
            while True:
                box_next = box + direction
                box_symbol = grid[box_next.y][box_next.x]
                if box_symbol == "#":
                    break
                elif box_symbol == '.':
                    box_moving_allowed = True
                    break
                box = box_next
                i += 1
            if not box_moving_allowed:
                continue
            grid[next_pos.y][next_pos.x] = "."
            for j in range(1, i+1):
                box_next = next_pos + (direction * j)
                grid[box_next.y][box_next.x] = "O"
        current_postition = next_pos
        # print_current_arrangement()
    
    # print_current_arrangement()

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "O":
                silver += 100*y + x  


    tmp_grid: list[list[str]] = [[c for c in line] for line in data[0]]
    grid: list[list[str]] = [[] for line in data[0]]

    replacement = {
        "#" : "##",
        "O" : "[]",
        "." : "..",
        "@" : "..",
    }

    print(tmp_grid)
    print_current_arrangement(tmp_grid)
    for y, row in enumerate(tmp_grid):
        for x, char in enumerate(row):
            for new_char in replacement[char]:
                if char == '@':
                    start_y = y
                    start_x = x*2
                grid[y].append(new_char)

    current_postition = Coordinate(start_x, start_y)
    grid[start_y][start_x] = '.'
    print_current_arrangement(grid, current_postition)

    for command in commands:
        direction = movement[command]
        next_pos = current_postition + direction
        symbol = grid[next_pos.y][next_pos.x]
        if symbol == "#":
            print_current_arrangement(grid, current_postition, command)
            continue
        elif symbol in ["[", "]"]:
            box_moving_allowed = False
            if direction in [Dirs.LEFT, Dirs.RIGHT]:
                i = 1
                box = next_pos
                while True:
                    box_next = box + direction*2
                    box_symbol = grid[box_next.y][box_next.x]
                    if box_symbol == "#":
                        break
                    elif box_symbol == '.':
                        box_moving_allowed = True
                        break
                    box = box_next
                    i += 1
                if not box_moving_allowed:
                    print_current_arrangement(grid, current_postition, command)
                    continue
                grid[next_pos.y][next_pos.x] = "."
                box_next = next_pos + direction
                for j in range(0, i):
                    grid[box_next.y][box_next.x] = "]" if direction == Dirs.LEFT else "["
                    box_next += direction
                    grid[box_next.y][box_next.x] =  "[" if direction == Dirs.LEFT else "]"
                    box_next += direction
            else:
                memory = {}
                x, y = next_pos.x, next_pos.y
                xs = set([x]) if symbol == "[" else set([x-1])
                # I call this a Push detection (and how to avoid recursives)
                # It's beautiful how awful the code can look when using while/for...else pattern too much
                memory[y] = xs.copy() 
                while len(xs):
                    y += 1 if direction == Dirs.DOWN else -1
                    new_xs = set()
                    while len(xs) and (box_start_x := xs.pop()) + 1:
                        for x in [box_start_x, box_start_x+1]:
                            char = grid[y][x]
                            if char == "#":
                                break
                            elif char == "]":
                                new_xs.add(x-1)
                            elif char in "[":
                                new_xs.add(x)
                        else:
                            continue
                        break   # If wall was found we end up here
                    else:
                        if len(new_xs):
                            xs = new_xs
                            memory[y] = xs.copy()
                        continue
                    break   # If wall was found we end up here
                else:
                    box_moving_allowed = True
                    print_current_arrangement(grid, current_postition, command)
                    # Moving boxes is allowed
                    y_diff = 1 if direction == Dirs.DOWN else -1
                    ys = sorted(list(memory), reverse=direction == Dirs.DOWN)
                    for y in ys:
                        xs = memory[y]
                        for x in xs:
                            grid[y][x] = "."
                            grid[y][x+1] = "."
                            grid[y+y_diff][x] = "["
                            grid[y+y_diff][x+1] = "]"
                    current_postition = next_pos
                print_current_arrangement(grid, current_postition, command)
                continue
        current_postition = next_pos
        print_current_arrangement(grid, current_postition, command)


    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "[":
                gold += 100*y + x  

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "test") 