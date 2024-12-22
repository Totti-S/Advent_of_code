import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (None, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    print(data)
    for line in data:
        pass

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")