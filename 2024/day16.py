import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
import utilities.directions as Dirs
import heapq

def debug_print(data, pos: Coordinate):
    with open("data/day16_screen.txt",'w') as f:
        for y, line in enumerate(data):
            if pos.y == y:
                print_string = line[:pos.x] + "O" + line[pos.x+1:]
            else:
                print_string = line
            f.write(print_string + "\n")

def debug_path(data, nodes: set[Coordinate]):
    with open("data/day16_screen.txt",'w') as f:
        for y, line in enumerate(data):
            nodes_with_y = [node for node in nodes if node.y == y]
            print_string = line
            for node in nodes_with_y:
                print_string = print_string[:node.x] + "O" + print_string[node.x+1:]
            f.write(print_string + "\n")

@testable(__file__, (11048, 64))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 1e12, 0

    for y, line in enumerate(data):
        if (x := line.find('S')) != -1:
            start_x = x
            start_y = y
        if (x := line.find('E')) != -1:
            end_x = x
            end_y = y

    end_point = Coordinate(end_x, end_y)
    reindeer = Coordinate(start_x, start_y)
    direction = Dirs.EAST
    points = 0
    visited: dict[tuple[Coordinate, Coordinate], int] = {(reindeer, direction) : 0}
    path = set[Coordinate]
    queue: list[tuple[int, Coordinate, Coordinate, set[Coordinate]]] = [(points, reindeer, direction, set())]

    # Find all crossroads

    # Solution:
    #   1: Make priority queue
    #   2. Take the lowest path score from queue
    #   3. Increment path score to to every directions, append those that are valid to queue
    #       a. Keep note of position and direction and allow only is lower score
    #   4. First time algorithm sees the end point: That's our solution

    # For gold:
    #   1. loosen the 3.a to allow duplicates for paths that have same score
    #   2. After first solution is found note the score: that's our upper bound
    #   3. Empty the queue and append paths that reach end point to memory
    #   4. Make set union of all possible paths to end point

    i = -1
    possible_paths: list[set[Coordinate]] = []
    while len(queue):
        i += 1
        points, reindeer, direction, path = heapq.heappop(queue)
        if points > silver:
            continue
        if reindeer == end_point:
            possible_paths.append(path)
            silver = points
        for next_dir in [direction, direction.rotate90(), direction.rotate90(True)]:
            next_step = reindeer + next_dir
            if data[next_step.y][next_step.x] in [".", "E"]:
                add_on = 1 if next_dir == direction else 1001
                if (next_step, next_dir) not in visited or points+add_on <= visited[(next_step, next_dir)]:
                    new_path = path.copy()
                    new_path.add(reindeer)
                    visited[(next_step, next_dir)] = points+add_on
                    heapq.heappush(queue, (points+add_on, next_step, next_dir, new_path))

    all_tile = set()
    for path in possible_paths:
        all_tile = all_tile | path

    gold = len(all_tile) + 1 # Start tiles
    print(f'{silver = }')
    print(f'{gold = }')
if __name__ == "__main__":
    main("both", "")