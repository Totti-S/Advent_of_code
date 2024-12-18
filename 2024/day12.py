import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
import utilities.directions as dirs

from collections import defaultdict

@testable(__file__, (140, 80), (1930, None), (772, 436))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    max_x, max_y = len(data[0]), len(data)

    letters: dict[str, list[list[Coordinate]]] = defaultdict(list)

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            node = Coordinate(x, y)
            if char not in letters:
                letters[char].append([node])
            else:
                regions = letters[char]
                connects_to = set()
                for coord in dirs.adj4(node):
                    if coord.x in [-1, max_x] or coord.y in [-1, max_y]:
                        continue
                    for k, region in enumerate(regions):
                        if coord in region:
                            connects_to.add(k)

                if len(connects_to) == 1:
                    regions[list(connects_to)[0]].append(node)
                elif len(connects_to) > 1:
                    combine_regions = []
                    for index in connects_to:
                        combine_regions += regions[index].copy()
                    letters[char] = [region for i, region in enumerate(regions) if i not in connects_to]
                    combine_regions.append(node)
                    letters[char].append(combine_regions)
                else:
                    regions.append([node])

    for regions in letters.values():
        for region in regions:
            node_set = set(region)
            # Find the perimeter by checking if there is node next to it,
            # if not, that's a perimeter fence
            perimeter = 0
            for node in node_set:
                for coord in dirs.adj4(node):
                    if coord not in node_set:
                        perimeter += 1
            area = len(node_set)
            silver += perimeter * area

    print(f'{silver = }')

    # It's gold time and it seems hard :(
    # We can re-use out regions, but we have to "scan" through slice by slice
    # OR at least thats the plan

    # Update.... Well f***. I spend one eternity to figure out away to slice the regions
    # and trying to figure out to count the edges with finding min and max from the slice
    # Obviously that will fail to the empty spots inside the region. Then I tried to figure
    # how to make the solution work still with little to no avail.

    def other_solution(region: list[Coordinate]):
        min_x = min(region, key=lambda x: x.x).x
        min_y = min(region, key=lambda x: x.y).y
        max_x = max(region, key=lambda x: x.x).x
        max_y = max(region, key=lambda x: x.y).y
        # Skip all the other nonsense if region shaped like a line
        if min_x == max_x or min_y == max_y:
            sides = 4
            return sides

        sides = 0 # Total
        # Let's look DOWN and UP per row cell by cell. (0 -> n) (0 -> n)
        # If we find cell that has no down neighbor then it has to be part of a side
        # Side ends if: the line breaks OR if we find neighbor
        for y in range(min_y, max_y+1):
            previous = -2
            walls = [False, False] # UP and DOWN
            line = sorted([coord.x for coord in region if coord.y == y])
            for x in line:
                if x - previous != 1:
                    walls = [False, False]
                for i, direction in enumerate([dirs.UP, dirs.DOWN]):
                    if Coordinate(x,y) + direction not in region:
                        if not walls[i]:
                            walls[i] = True
                            sides += 1
                    else:
                        walls[i] = False
                previous = x
        # Now do this to RIGHT and LEFT directions as well
        for x in range(min_x, max_x+1):
            previous = -2
            walls = [False, False] # LEFT and RIGHT
            line = sorted([coord.y for coord in region if coord.x == x])
            for y in line:
                if y - previous != 1:
                    walls = [False, False]
                for i, direction in enumerate([dirs.LEFT, dirs.RIGHT]):
                    if Coordinate(x,y) + direction not in region:
                        if not walls[i]:
                            walls[i] = True
                            sides += 1
                    else:
                        walls[i] = False
                previous = y
        return sides

    for regions in letters.values():
        for region in regions:
            gold += other_solution(region) * len(region)

    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")