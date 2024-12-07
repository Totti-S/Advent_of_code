import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import test

from collections import Counter
import re

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    silver, gold = 0, 0

    vowels = "aeiou"
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for line in data:
        occurances = Counter(line)
        if sum([occurances[v] for v in vowels]) < 3:
            continue
        if any([string in line for string in forbidden]):
            continue
        
        char = line[0]
        for c in line[1:]:
            if c == char:
                break
            char = c
        else:
            continue
        silver += 1

    for line in data:
        if len(re.findall(r'([a-z][a-z])(?=.*\1)', line)) and len(re.findall(r'([a-z])(?=.\1)', line)):
            gold += 1

    print(f'{silver = }')
    print(f'{gold = }')

if __name__ == "__main__":
    main("both", '')
    test(main, __file__, (2, None), (None, 2))