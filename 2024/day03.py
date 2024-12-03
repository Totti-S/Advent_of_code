import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode

import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    data: str = "".join(data)
    total = 0
    commands: list[re.Match]
    acceptable_commands: list[str] = []

    commands = list(re.finditer(r'mul\(\d+\,\d+\)', data))
    for command in commands:
        start_idx = command.start()
        behind_line = data[:start_idx]
        behind_line = behind_line[::-1]

        yes = behind_line.find(")(od")
        no = behind_line.find(")(t'nod")
        if no == -1 or (yes < no and yes != -1) or mode == "silver":
            acceptable_commands.append(command.group())

    for command in acceptable_commands:
        numbers = command.lstrip("mul(").rstrip(')').split(",")
        numbers = list(map(int, numbers))
        total += int(numbers[0]) * int(numbers[1])

    print(f'{mode} : {total}')

if __name__ == "__main__":
    main(mode="gold", data_type='')