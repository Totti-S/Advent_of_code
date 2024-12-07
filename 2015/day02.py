import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test
from utilities.helper_funs import nums

from math import prod

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    def surface(L: int, W: int, H: int):
        sides = [L*W, W*H, H*L]
        # print(sides, 2*sum(sides), min(sides))
        return 2*sum(sides) + min(sides)
    
    def ribbon(sides: list[int]):
        sides.sort()
        return 2*sum(sides[:2]) + prod(sides)

    print(data)
    for line in data:
        sides = nums(line.split('x'))
        silver += surface(*sides)
        gold += ribbon(sides)
        

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both", data_type='')
    test(main, __file__, (101, 48))