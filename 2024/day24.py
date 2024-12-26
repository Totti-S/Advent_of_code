from operator import and_, or_, xor
import re
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

operators = {
    "AND" : and_,
    "OR" : or_,
    "XOR": xor,
}

@testable(__file__, (2024, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, has_portions=True)
    silver, gold = 0, 0

    xs_and_ys, unparsed_commands = data
    directory: dict[str, int] = {}
    for inital_state in xs_and_ys:
        results: re.Match = re.search(r'([x|y]\d+): (\d)', inital_state)
        name = results.group(1)
        bit = int(results.group(2))
        directory[name] = bit

    commands = []
    for command in unparsed_commands:
        result: re.Match = re.search(r'(...) (AND|OR|XOR) (...) -> (...)', command)
        input1 = result.group(1)
        operator = operators[result.group(2)]
        input2 = result.group(3)
        output = result.group(4)
        commands.append((input1, operator, input2, output))

    found = 1
    while len(commands) and found:
        i = 0
        found = 0
        while i < len(commands):
            if commands[i][0] in directory and commands[i][2] in directory:
                found += 1
                in1, oper, in2, out = commands.pop(i)
                directory[out] = oper(directory[in1], directory[in2])
            i += 1

    print(f"{commands = }")
    for k, v in directory.items():
        if k.startswith("z") and v:
            silver += 2**int(k[1:3])

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")