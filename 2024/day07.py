import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test
from utilities.helper_funs import nums
from collections.abc import Generator
from itertools import product

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    def all_results(numbers: list[int], concat: bool = False) -> Generator[int, None, None]:
        # From a wiser man (https://github.com/ththarkonen) I was reminded of 'product()' function
        operators = "+*"
        if concat:
            operators += "|"
        
        for perm in product(operators, repeat=len(numbers)-1):
            val = numbers[0]
            if concat and "|" not in perm: # Small optimization
                continue
            for number, operator in zip(numbers[1:], perm):
                if operator == '+':
                    val += number
                elif operator == '*':
                    val *= number
                else:
                    val = int(f"{val}{number}")
            yield val

    for line in data:
        result, others = line.split(':')
        result = int(result)
        numbers = nums(others.strip().split(' '))
        
        if any((result == res) for res in all_results(numbers)):
            silver += result
        elif any((result == res) for res in all_results(numbers, concat=True)):
            gold += result
    
    gold += silver

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", '')
    test(main, __file__, (3749, 11387))