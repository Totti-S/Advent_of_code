import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import test

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    max_y = len(data)
    max_x = len(data[0])
    
    # data = [[char for char in line] for line in data]
    all_different_antannae = set([char for line in data for char in line])
    all_different_antannae.remove('.')

    nodes = set()
    harmonics = set()
    for antanna in all_different_antannae:
        coords: list[Coordinate] = []
        for y, line in enumerate(data):
            if (x := line.find(antanna)) != -1:
                coords.append(Coordinate(x, y))
        
        for i, coord in enumerate(coords[:-1]):
            for j, coord2 in enumerate(coords[i+1:]):
                harmonics.add(coord)
                harmonics.add(coord2)
                vec = coord - coord2
                first = coord + vec
                if 0 <= first.x < max_x and 0 <= first.y < max_y:
                    nodes.add(first)
                second = coord2 - vec
                if 0 <= second.x < max_x and 0 <= second.y < max_y:
                    nodes.add(second)

                while True:
                    first = first + vec
                    if found_first := (0 <= first.x < max_x and 0 <= first.y < max_y):
                        harmonics.add(first)

                    second = second - vec
                    if found_second := (0 <= second.x < max_x and 0 <= second.y < max_y):
                        harmonics.add(second)

                    if not found_first and not found_second:
                        break
                

    silver = len(nodes)
    gold = len(nodes.union(harmonics))

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", '')
    test(main, __file__, (14, 34), (None,9))