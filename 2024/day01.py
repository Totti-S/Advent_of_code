from utilities.get_data import get_data
from utilities.alias_type import Mode

import operator
from collections import Counter

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=True)

    left, right = [], []
    for x, y in data:
        left.append(x)
        right.append(y)

    if mode == 'silver' or mode == 'both':
        left.sort()
        right.sort()
        distances = [abs(d) for d in map(operator.sub, left, right)]
        total = sum(distances)
        print(f'silver : {total}')

    if mode == 'gold' or mode == 'both':
        occurances = Counter(right)
        multi = [num * occurances[num] for num in left]
        total = sum(multi)
        print(f'gold : {total}')

if __name__ == "__main__":
    main(mode='both', data_type='')