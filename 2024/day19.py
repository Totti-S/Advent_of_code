import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode
from utilities.test_framework import testable

@testable(__file__, (6, 16), (None, 12), before=False, after=True)
def main(mode: Mode ='both', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=False, has_portions=True)
    silver, gold = 0, 0

    patterns, designs = data
    patterns = set([pattern.strip() for pattern in patterns[0].split(',')])
    not_solution = set()
    gold_cache: dict[str, int] = {}

    def recursive_function(design_left: str) -> bool:
        current_towel = ""
        i = 0
        while i < len(design_left):
            current_towel += design_left[i]
            if current_towel in patterns:
                if len(design_left[i+1:]) == 0:
                    return True
                elif recursive_function(design_left[i+1:]):
                    return True
            i += 1
        return False

    def gold_recursive(design_left: str, hits: int) -> int:
        current_towel = ""
        i = 0
        while i < len(design_left):
            current_towel += design_left[i]
            if current_towel in patterns:
                if len(design_left[i+1:]) == 0:
                    hits += 1
                    return hits
                else:
                    if design_left[i+1:] in not_solution:
                        continue
                    elif design_left[i+1:] in gold_cache:
                        hits += gold_cache[design_left[i+1:]]
                    else:
                        solution = gold_recursive(design_left[i+1:], 0)
                        if solution == 0:
                            not_solution.add(design_left[i+1:])
                        else:
                            gold_cache[design_left[i+1:]] = solution
                        hits += solution
            i += 1
        return hits


    for design in designs:
        if recursive_function(design):
            silver += 1

    for design in designs:
        current_towel = ""
        i = 0
        while i < len(design):
            current_towel += design[i]
            if current_towel in patterns:
                if len(design[i+1:]) == 0:
                    gold += 1
                    continue
                elif design[i+1:] in not_solution:
                    continue
                elif design[i+1:] in gold_cache:
                    gold += gold_cache[design[i+1:]]
                hits = gold_recursive(design[i+1:], 0)
                if hits == 0:
                    not_solution.add(design[i+1:])
                else:
                    gold_cache[design[i+1:]] = hits
                gold += hits
            i += 1

    print(f'{silver = }')
    print(f'{gold = }')
    # Too low; 524173293165589
if __name__ == "__main__":
    main("both", "test")