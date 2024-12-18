import re
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
from utilities.helper_funs import nums
import utilities.directions as dirs
import heapq

@testable(__file__, (22, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    all_corrupted_spaces = []
    for line in data:
        x, y = nums(re.findall('\d+', line))
        all_corrupted_spaces.append(Coordinate(x,y))

    current_position = Coordinate(0,0)
    if data_type == "test":
        end_postition = Coordinate(6,6)
        max_x = max_y = 6
        silver_corrupt = set(all_corrupted_spaces[:12])
    else:
        end_postition = Coordinate(70,70)
        max_x = max_y = 70
        silver_corrupt = set(all_corrupted_spaces[:1024])

    # Mostly reused day16 answer.
    # First time we hit the end point we have optimal answer
    length = 0
    seen = set([current_position])
    prio_que = [(0, current_position)]
    while len(prio_que):
        length, node = heapq.heappop(prio_que)
        if node == end_postition:
            break
        for next_node in dirs.adj4(node):
            if -1 < next_node.x <= max_x and -1 < next_node.y <= max_y and next_node not in silver_corrupt | seen:
                seen.add(next_node)
                heapq.heappush(prio_que, (length + 1, next_node))

    silver = length

    # For gold I reused code somewhat from day12 to combine regions.
    # Solution: First time when chain of adjacent corrupted bits reaches grid bounds
    #           so that it wall of all possible paths. Only 2 "walling off" chains
    #           are unvalid breaks -> if min_x -> max_y or min_y -> max_x
    keys = [
        lambda x:x.x,
        lambda x:x.y,
    ]
    current_bit_set = set()
    regions: list[list[Coordinate]] = []
    for bit in all_corrupted_spaces:

        connects_to: set[int] = set()
        for adj_bit in dirs.adj8(bit):
            if adj_bit in current_bit_set:
                for i, region in enumerate(regions):
                    if adj_bit in region:
                        break
                connects_to.add(i)

        current_bit_set.add(bit)
        if len(connects_to) == 0:
            regions.append([bit])
            continue

        if len(connects_to) == 1:
            index = list(connects_to)[0]
            regions[index].append(bit)
            r = regions[index]
        else:
            # Connecting chains
            combine_regions = []
            for index in connects_to:
                combine_regions += regions[index].copy()
            regions = [region for i, region in enumerate(regions) if i not in connects_to]
            combine_regions.append(bit)
            regions.append(combine_regions)
            r = regions[-1]

        if min(r, key=keys[0]).x == 0 and (max(r, key=keys[0]).x == max_x or min(r, key=keys[1]).y == 0):
            break
        if max(r, key=keys[1]).y == max_y and (min(r, key=keys[1]).y == 0 or max(r, key=keys[0]).x == max_x):
            break
    else:
        print("Ei löytynyt")

    print(f'{silver = }')
    print(f'gold: {bit.x},{bit.y}')

if __name__ == "__main__":
    main("both", "")