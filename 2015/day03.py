from collections import defaultdict
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode, Coordinate
from utilities.test_framework import test

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    data = data[0]

    current_house = Coordinate(0,0)
    gifts_per_house = defaultdict(int)
    gifts_per_house[current_house] += 1
    dirs = {
        ">" : Coordinate.RIGHT,
        "<" : Coordinate.LEFT,
        "v" : Coordinate.DOWN,
        "^" : Coordinate.UP,
    }
    for char in data:
        current_house += dirs[char]
        gifts_per_house[current_house] += 1
    
    silver = len(gifts_per_house)

    current_santa = Coordinate(0,0)
    current_robo = Coordinate(0,0)
    gifts_per_house = defaultdict(int)
    gifts_per_house[current_santa] += 1

    print(len(data))
    iteror = iter(data)
    i = 0
    for char in iteror:
        i += 1
        current_santa += dirs[char]
        char = next(iteror)
        current_robo += dirs[char]
    
        gifts_per_house[current_santa] += 1
        gifts_per_house[current_robo] += 1

    print(i)

    gold = len(gifts_per_house)

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both")
    test(main, __file__, (2, 11), (4, 3))