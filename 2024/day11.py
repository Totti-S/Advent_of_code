from re import A
import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (55312, None), (55312, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=True)
    silver, gold = 0, 0
    stone_list = data[0].copy()

    new_stone_list: list[int] = []

    for i in range(25):
        for stone in stone_list:
            # Rules
            # First rule:  0 -> 1
            if stone == 0:
                new_stone_list.append(1)
            # Second rule: Even length number split in two
            elif (length := len(stone_str :=str(stone))) % 2 == 0:
                stone = int(stone_str[:length // 2])
                new_stone = int(stone_str[length // 2:])
                new_stone_list += [stone, new_stone]
            # Third rule: Everything else fails, multiply by 2024 (I have bad feeling about this 2^11)
            else:
                new_stone_list.append(stone * 2024)

        stone_list = new_stone_list.copy()
        new_stone_list.clear()

    silver = len(stone_list)

    # Recursive GÄNG, or is it too late for that?
    # cache: dict[tuple[int, int], list[int]] = {}
    # def recursive_fun(value, depth, number_trail: list[int]):
    #     if depth >= 76:
    #         return [value]
    #     # Rules
    #     # First rule:  0 -> 1
    #     new_list = []
    #     if value == 0:
    #         new_list += recursive_fun(1, depth=depth+1)
    #     elif (value, 75 - depth) in cache:
    #         return cache[(value, 75 - depth)]
    #     elif (value, 1) in cache:
    #         new_list += cache[(value, 1)]
    #     # Second rule: Even length number split in two
    #     elif (length := len(stone_str :=str(value))) % 2 == 0:
    #         left = int(stone_str[:length // 2])
    #         right = int(stone_str[length // 2:])
    #         new_list += [left, right]
    #         cache[(value, 1)] = [left, right]
    #     # Third rule: Everything else fails, multiply by 2024 (I have bad feeling about this 2^11)
    #     else:
    #         new_list += [value * 2024]
    #         cache[(value, 1)] = [left, right]

    #     for


    # stone_list = data[0].copy()
    # new_stone_list: list[int] = []
    # # Let me just say that I guessed that this was happening
    # for i in range(75):
    #     for stone in stone_list:

    #     stone_list = new_stone_list.copy()
    #     print(i)
    #     new_stone_list.clear()

    # gold = len(stone_list)
    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")