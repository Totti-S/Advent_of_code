import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0
    data = data[0]
    print(data)
    print(data.count("("),  data.count(")"))
    silver = data.count("(") - data.count(")")

    floor = 0
    for i, char in enumerate(data, 1):
        floor += 1 if char == "(" else -1
        if floor == -1:
            gold = i
            break

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both")
    # test(main, __file__, (None, None))