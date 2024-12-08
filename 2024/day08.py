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
        
        if len(coords) < 2:
            continue

        harmonics.update(coords)
        for i, coord in enumerate(coords[:-1]):
            for coord2 in coords[i+1:]:
                j = -1
                vec = coord - coord2
                node_coords = [coord, coord2]
                while (j := j + 1) + 1:
                    found = False
                    for k in range(2):
                        node_coords[k] += vec if not k else vec * -1
                        node = node_coords[k]
                        if 0 <= node.x < max_x and 0 <= node.y < max_y:
                            found = True
                            if not j:
                                nodes.add(node)
                            else:
                                harmonics.add(node)
                    if not found:
                        break

    silver = len(nodes)
    gold = len(nodes | harmonics)

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", '')
    test(main, __file__, (14, 34), (None,9))