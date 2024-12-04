import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test

import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    # Silver solution:  Find all the 'XMAS' with regex. The data needs to
    #                   be transposed and converted to diagonal

    i_max = len(data)

    transposed = ["." * i_max for _ in range(i_max)]
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            transposed[j] = transposed[j][:i] + char + transposed[j][i+1:]

    diagonal = []
    for i in range(i_max):
        left_up = ""
        left_down = ""
        right_up = ""
        right_side_down = ""

        for j in range(0, i+1):
            left_up += data[i-j][j]
            left_down += data[i_max-1-j][i - j]
            right_up += data[i-j][i_max-1 - j]
            right_side_down += data[i_max-1-j][i_max-1 -i + j]

        diagonal.append(left_up)
        diagonal.append(right_up)
        # Remove the duplicate string
        if i != i_max-1:
            diagonal.append(left_down)
            diagonal.append(right_side_down)

    for line in data + transposed + diagonal:
        silver += len(re.findall(r'XMAS', line))
        silver += len(re.findall(r'SAMX', line))

    print(f'{silver = }')

    # Gold solution:    find all the A:s in inner square and find out
    #                   if the corners are "M" or "S".

    for i, line in enumerate(data[1:-1], 1):
        for j, char in enumerate(line[1:-1], 1):
            if char != 'A':
                continue
            left_up = data[i-1][j-1]
            left_down = data[i+1][j-1]
            right_up = data[i-1][j+1]
            right_down = data[i+1][j+1]

            if left_up not in ["S", "M"]:
                continue
            if left_down not in ["S", "M"]:
                continue
            if right_down not in ["S", "M"]:
                continue
            if right_up not in ["S", "M"]:
                continue
            if left_up == right_down or right_up == left_down:
                continue
            gold += 1

    print(f'{gold = }')

if __name__ == "__main__":
    main(mode="both", data_type="")
    test(main, __file__, (18, 9))