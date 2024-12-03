import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode

import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    print(data)
    commands : list[str]
    total = 0
    for line in data:
        commands = re.findall(r'mul\(\d+\,\d+\)', line)

        for command in commands:
            numbers = command.lstrip("mul(").rstrip(')').split(",")
            numbers = list(map(int, numbers))
            total += int(numbers[0]) * int(numbers[1])




    print(f'{mode} : {total}')

if __name__ == "__main__":
    main(data_type='')