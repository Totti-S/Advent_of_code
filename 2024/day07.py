import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test
from utilities.helper_funs import nums
from math import prod
from collections.abc import Generator

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    # Felt very lazy, so pulled this from here: https://stackoverflow.com/a/34559825
    def ternary(n: int) -> str:
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))

    def all_results(numbers: list[int], base3: bool =False) -> Generator[int, None, None]:
        base = 3 if base3 else 2 
        total = base**(len(numbers)-1) - 1
        for perm in range(1,total):
            if base3:
                perm = ternary(perm).zfill(len(numbers)-1)
                # Optimization: we have tested all values that dosen't contain '2'
                if '2' not in perm:
                    continue
            else:
                perm = f"{perm:b}".zfill(len(numbers)-1)
            val = numbers[0]
            for number, operator in zip(numbers[1:], perm):
                if operator == '0':
                    val += number
                elif operator == '1':
                    val *= number
                else:
                    val = int(f"{val}{number}")
            yield val

    for line in data:
        result, others = line.split(':')
        result = int(result)
        numbers = nums(others.strip().split(' '))

        if sum(numbers) == result or prod(numbers) == result:
            silver += result
            continue
        elif int(others.replace(' ', '')) == result:
            gold += result
            continue
        elif len(numbers) == 2:
            continue
        
        for res in all_results(numbers):
            if res == result:
                silver += result
                break
        else:
            for res in all_results(numbers, base3=True):
                if res == result:
                    gold += result
                    break
    
    gold += silver

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", '')
    test(main, __file__, (3749, 11387))