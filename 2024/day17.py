import re
import sys
from time import sleep
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable
from utilities.helper_funs import nums


# @testable(__file__, (None, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, has_portions=True)
    # silver, gold = 0, 0

    registers, program = data
    A = int(re.findall(r'\d+', registers[0])[0])
    B = int(re.findall(r'\d+', registers[1])[0])
    C = int(re.findall(r'\d+', registers[2])[0])
    instructions = nums(re.findall(r'\d', program[0]))

    print(A,B,C, instructions)

    def computer(registers, check_output: list | None = None):
        A, B, C = registers
        operands = {
            0: lambda: 0,
            1: lambda: 1,
            2: lambda: 2,
            3: lambda: 3,
            4: lambda: A,
            5: lambda: B,
            6: lambda: C,
        }
        pointer = 0
        output = []
        i = 0
        while pointer+1 < len(instructions):

            instruction = instructions[pointer]
            literal = instructions[pointer +1]
            combo = operands[instructions[pointer +1]]()
            match instruction:
                case 0:
                    A = A // (2**combo)
                case 1:
                    B = B ^ literal
                case 2:
                    B = combo % 8
                case 3:
                    if A != 0 and literal != pointer:
                        pointer = literal
                        continue
                case 4:
                    B = B ^ C
                case 5:
                    val = str(combo % 8)
                    if check_output and int(val) != check_output[i]:
                        break
                    output.append(str(combo % 8))
                    i += 1
                case 6:
                    B = A // (2**combo)
                case 7:
                    C = A // (2**combo)
            pointer += 2
        return output

    silver = computer([A, B, C])
    gold = computer([117440, B, C], instructions)

    j = 0
    while True:
        # print([j, B, C])
        check = computer([j, B, C], instructions)
        if nums(check) == instructions:
            break
        # if j == 117440:
        #     print(check)
        #     sleep(10)

        j += 1
        # print(j)
    gold = j

    print(",".join(silver))
    print(f"{program = } , {check = }")
    print()
    # print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")