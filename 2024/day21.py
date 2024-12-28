import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable


@testable(__file__, (126384, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0


    transformer: dict[str, str] = {
        "A^": "<",
        "Av": "<v",
        "A<": "v<<",
        "A>": "v",
        "^A": ">",
        "^>": "v>",
        "^v": "v",
        "^<": "v<",
        "<A": ">>^",
        "<^": ">^",
        "<>": ">>",
        "<v": ">",
        "vA": "^>",
        "v>": ">",
        "v^": "^",
        "v<": "<",
        ">A": "^",
        ">^" : "^<",
        ">v" : "<",
        "><" : "<<",
    }

    def pad2num(pad: str) -> int:
        if pad == "A":
            return -1
        elif pad == "0":
            return -2
        return int(pad) - 1

    def calculate_commands(start: str, end: str) -> tuple[int, int]:
        start = pad2num(start)
        end = pad2num(end)

        y_s, x_s = divmod(start, 3)
        y_e, x_e = divmod(end, 3)

        Δx = x_e - x_s
        Δy = y_s - y_e
        x_str = ">"  * Δx if Δx >= 0 else "<" * abs(Δx)
        y_str = "v" * Δy if Δy >= 0 else "^" * abs(Δy)

        if start == -2:
            return y_str + x_str
        elif start == -1 and Δx == -1:
            return x_str + y_str
        elif start in [1, 4, 7] and Δx > 0 and Δy > 0:
            return y_str + x_str
        elif (Δy <= -1 and Δx <= -1 and start >= 0) or Δy > 0:
            return x_str + y_str
        else:
            return y_str + x_str
    # 237710 too high
    # 227898 too high

    def calculate_pad_orders(commands: str) -> str:
        i = 0
        previous_command = "A"
        sequence = ""
        while i < len(commands):
            next_command = commands[i]
            if next_command == previous_command:
                sequence += "A"
                i += 1
                continue
            sequence += transformer[previous_command + next_command] + "A"
            previous_command = next_command
            i += 1
        return sequence


    print(data)
    for line in data:
        position = "A"
        total_sequence = ""
        # print(line)
        for char in line:
            first_order_commands = calculate_commands(position, char) + "A"
            position = char
            second_order_commands = calculate_pad_orders(first_order_commands)
            seq = calculate_pad_orders(second_order_commands)
            total_sequence += seq

        print(f"{line} : {total_sequence}")
        print(len(total_sequence), int(line[0:3]))
        silver += int(line[0:3]) * len(total_sequence)

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")