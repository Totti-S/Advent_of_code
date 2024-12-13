import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable
from utilities.helper_funs import nums
import re
from scipy.optimize import linprog
from numpy.linalg import det, inv, matmul

@testable(__file__, (480, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False, has_portions=True)
    silver, gold = 0, 0

    def solve_LP(bounds: tuple[None | int] = (0, 100), gold: bool = False) -> int:
        total = 0
        for portion in data:
            A, b = [[], []], []
            for i, line in enumerate(portion):
                tmp = nums(re.findall(r'\d+', line))
                if i < 2:
                    A[0].append(tmp[0])
                    A[1].append(tmp[1])
                else:
                    b = tmp
                    if gold:
                        add_on = int(1e13)
                        b[0] += add_on
                        b[1] += add_on
            result = linprog([3,1], A_eq=A, b_eq=b, bounds=bounds, integrality=[1,1], method='highs')
            if result.success:
                total += int(result.fun)
        return total

    # silver = solve_linear()
    wrong_gold = solve_LP((0, None), gold=True)
    print(f'{wrong_gold = }')

    # Man can be stupid at times. Why do this in LP-way, when this is just
    # Two functions -> Convert constraints to matrix -> If inverse can be found, solution can be also
    # -> Matrix multiplication, some rounding and voilà .

    def solve_inverse(gold: bool = False) -> int:
        total = 0
        for j, portion in enumerate(data):
            A, b = [[], []], []
            for i, line in enumerate(portion):
                tmp = nums(re.findall(r'\d+', line))
                if i < 2:
                    A[0].append(tmp[0])
                    A[1].append(tmp[1])
                else:
                    b = tmp
                    if gold:
                        b[0] += int(1e13)
                        b[1] += int(1e13)
            if det(A) != 0:
                inv_A = inv(A)
                variables = matmul(inv_A, b)
                variables: list[float] = list(map(float, variables)) # I like numpy, but not its types
                if not gold and any(val > 100 for val in variables):
                    continue
                if all(abs(val - round(val)) < 1e-3 for val in variables):
                    total += round(variables[0]) * 3 + round(variables[1])
        return int(total)

    silver = solve_inverse()
    gold = solve_inverse(True)
    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")