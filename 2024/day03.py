import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode

import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    data: str = "".join(data)
    commands: list[re.Match]
    acceptable_commands: list[str] = []
    all_commands: list[str] = []

    commands: list[re.Match] = list(re.finditer(r'mul\(\d+\,\d+\)', data))
    for command in commands:
        start_idx = command.start()

        yes = data[:start_idx].rfind("do()")
        no = data[:start_idx].rfind("don't")
        # For gold solution
        if no == -1 or (yes > no and yes != -1):
            acceptable_commands.append(command.group())
        # For silver solution
        all_commands.append(command.group())


    def process_commands(commands: list[str]) -> int:
        total = 0
        for command in commands:
            numbers = command.lstrip("mul(").rstrip(')').split(",")
            numbers = list(map(int, numbers))
            total += int(numbers[0]) * int(numbers[1])
        return total

    if mode in ["silver", "both"]:
        silver = process_commands(all_commands)
        print(f'{silver=}')

    if mode in ["gold", "both"]:
        gold = process_commands(acceptable_commands)
        print(f'{gold=}')

if __name__ == "__main__":
    main(mode="both", data_type='')