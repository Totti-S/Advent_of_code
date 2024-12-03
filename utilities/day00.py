import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    print(data)
    for line in data:
        pass

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both")
    test(main, __file__, (None, None))