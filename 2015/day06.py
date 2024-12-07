import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test
from utilities.helper_funs import nums

import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    
    toggled_on = set()
    
    # print(data)
    splitted: re.Match
    for line in data:
        splitted = re.search(r'(toggle|turn off|turn on) (\d+,\d+) through (\d+,\d+)', line).groups()
        min_x, min_y = nums(splitted[1].split(","))
        max_x, max_y = nums(splitted[2].split(","))
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                light = (i, j)
                match splitted[0]:
                    case "turn on":
                        toggled_on.add(light)
                    case "turn off":
                        toggled_on.discard(light)
                    case "turn toggle":
                        if light in toggled_on:
                            toggled_on.discard(light)
                        else:
                            toggled_on.add(light)
    silver = len(toggled_on)
    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both")
    test(main, __file__, (None, None))