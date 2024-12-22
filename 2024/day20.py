from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
import utilities.directions as Dirs

# @testable(__file__, (None, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    track_length = 0
    for y, line in enumerate(data):
        track_length += line.count(".")
        if (x := line.find('S')) != -1:
            start_x = x
            start_y = y
        if (x := line.find('E')) != -1:
            end_x = x
            end_y = y

    max_x, max_y = len(data[0]), len(data)

    end = Coordinate(end_x, end_y)
    start = Coordinate(start_x, start_y)

    lengths: dict[Coordinate, int] = {}
    lengths[start] = track_length
    lengths[end] = 0

    current = Coordinate(start_x, start_y)
    length = track_length
    track: list[Coordinate] = [current]
    previous_node = None
    while length:
        for next_node in Dirs.adj4(current):
            if data[next_node.y][next_node.x] in [".", 'E'] and next_node != previous_node:
                previous_node = current
                current = next_node
                lengths[current] = length - 1
                track.append(current)
                break
        length -= 1

    cheats = defaultdict(int) 
    for node in track:
        for cheat_node in Dirs.adj4(node, 2):
            if -1 < cheat_node.x < max_x and -1 < cheat_node.y < max_y:
                if data[cheat_node.y][cheat_node.x] in [".", 'E']:
                    if (time_skip := lengths[node] - lengths[cheat_node]) != 2:
                        cheats[time_skip] += 1

    for k, v in cheats.items():
        if k-2 >= 100:
            silver += v
        # if k > 0:
        #     print(k-2, v)

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")