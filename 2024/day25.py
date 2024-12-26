import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (3, None))
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, has_portions=True)
    silver, gold = 0, 0

    print(data)
    keys = []
    locks = []
    for lock_or_key in data:
        hit_symbol = "." if lock_or_key[0] == "#####" else "#"
        indcies = [None] * 5
        for i, row in enumerate(lock_or_key):
            for j, column in enumerate(row):
                if column == hit_symbol and indcies[j] is None:
                    indcies[j] = i - 1

        # assert all(i for i in indcies), f"{indcies = }"
        if lock_or_key[0] == "#####":
            locks.append(indcies)
        else:
            keys.append(indcies)

    for lock in locks:
        for key in keys:
            if all(val >= 0 for val in [k - L for k, L in zip(key, lock)]):
                silver += 1

    print(f'{silver = }')
    # print(f'{gold = }')

if __name__ == "__main__":
    main("both", "")