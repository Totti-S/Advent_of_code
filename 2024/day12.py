import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import testable
from utilities.directions import UP, DOWN, LEFT, RIGHT

from collections import defaultdict

@testable(__file__, (140, 80), (1930, None), (772, 436))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    max_x, max_y = len(data[0]), len(data)

    def check_coordinates(node: Coordinate) -> list[Coordinate]:
        return [node + UP, node + DOWN, node + LEFT, node + RIGHT]

    letters: dict[str, list[list[Coordinate]]] = defaultdict(list)

    print()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            node = Coordinate(x, y)
            if char not in letters:
                letters[char].append([node])
            else:
                regions = letters[char]
                connects_to = set()
                for coord in check_coordinates(node):
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


    print(letters)
    for letter, regions in letters.items():
        for region in regions:
            node_set = set(region)
            # Find the perimeter by checking if there is node next to it,
            # if not, that's a perimeter fence
            perimeter = 0
            for node in node_set:
                for coord in check_coordinates(node):
                    if coord not in node_set:
                        perimeter += 1

            area = len(node_set)
            print(f"{letter} : {perimeter* area}, {area = } , {perimeter = }")
            silver += perimeter * area

    print(f'{silver = }')



    # It's gold time and it seems hard :(
    # We can re-use out regions, but we have to "scan" through slice by slice
    # OR at least thats the plan

    # Vertical scan through left to right
    def vertical(region:list[Coordinate]) -> int:
        # Find region absolute boundaries
        min_x = min(region, key=lambda x: x.x).x
        min_y = min(region, key=lambda x: x.y).y
        max_x = max(region, key=lambda x: x.x).x
        max_y = max(region, key=lambda x: x.y).y

        # Skip all the other nonsense if region shaped like a line
        if min_x == max_x or min_y == max_y:
            sides = 2
            return sides

        min_of_slice = -1 # Outside of the boundary
        max_of_slice = max_y + 1
        sides = 0
        last_missing_spots = []
        last_missing_spots_in_regions = []
        for x in range(min_x, max_x+1):
            sub_region_ys = [coord.y for coord in region if coord.x == x]
            if min_of_slice != (new_min := min(sub_region_ys)):
                sides += 1
                min_of_slice = new_min
            if max_of_slice != (new_max := max(sub_region_ys)):
                sides += 1
                max_of_slice = new_max

            missing_from_slice = [y for y in range(min_of_slice+1, max_of_slice) if y not in sub_region_ys]
            if missing_from_slice == last_missing_spots:
                continue
            elif len(missing_from_slice) == 0:
                last_missing_spots = []
            elif len(last_missing_spots) == 0 or all(miss not in last_missing_spots for miss in missing_from_slice):
                sub_regions = 0
                missing_from_slice.sort()
                for y in missing_from_slice:
                    if y-1 not in missing_from_slice:
                        sub_regions += 1
                sides += sub_regions *2
                last_missing_spots = missing_from_slice.copy()
            else:
                # Last one to be made have to match sub regions
                # Find by finding matching elemets by comparing "missing" and "last"
                # min_region and max_region changes mean that +1 side
                # Somehow take in account the bigger group "eating" two groups together
                #   -> this means no sides were added
                pass


                subs: list[list[int]] = []
                for sub in subs:
                    if y-1 in sub:
                        sub.append(y)
                        break
                else:
                    subs.append([y])
        return sides
    def horizontal(region:list[Coordinate]) -> int:
        # Find region absolute boundaries
        min_x = min(region, key=lambda x: x.x).x
        min_y = min(region, key=lambda x: x.y).y
        max_x = max(region, key=lambda x: x.x).x
        max_y = max(region, key=lambda x: x.y).y

        # Skip all the other nonsense if region shaped like a line
        if min_x == max_x or min_y == max_y:
            sides = 2
            return sides

        min_of_slice = -1 # Outside of the boundary
        max_of_slice = max_x + 1
        sides = 0
        for y_index in range(min_y, max_y+1):
            sub_region = [coord for coord in region if coord.y == y_index]
            if min_of_slice != (new_min := min(sub_region, key=lambda x: x.x).x):
                sides += 1
                min_of_slice = new_min
            if max_of_slice != (new_max := max(sub_region, key=lambda x: x.x).x):
                sides += 1
                max_of_slice = new_max
        return sides

    for letter, regions in letters.items():
        for region in regions:
            v = vertical(region)
            h = horizontal(region)
            total_fence_cost = len(region) * (v+h)
            print(f"{letter} : {v = }, {h = } total: {v+h}, cost: {total_fence_cost}")
            gold += total_fence_cost


    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "test3")