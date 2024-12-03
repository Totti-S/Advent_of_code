import sys
sys.path.append('..')
from utilities.get_data import get_data
from utilities.alias_type import Mode

def main(mode: Mode ='silver', data_type: str = ''):
    data = get_data(__file__, data_type, line_is_numbers=True)

    def is_safe(line: list[int], boolean: bool = False) -> list[int] | bool:
        bad_indicies = set()
        positive_increment = None
        for i, (num, next_num) in enumerate(zip(line[:-1], line[1:])):
            diff = next_num - num
            if diff == 0 or abs(diff) > 3:
                if boolean:
                    return False
                bad_indicies.update([i, i+1])
            if positive_increment is None:
                positive_increment = diff > 0
            if positive_increment ^ (diff > 0): # XOR
                if boolean:
                    return False
                bad_indicies.update([i-1, i, i+1]) # 'i-1' This address the Test case: "93 95 92 91 90"
        return bad_indicies if not boolean else True


    all_bad_indicies = [is_safe(line) for line in data]
    silver = sum(not bool(one_list) for one_list in all_bad_indicies)
    if mode in ["silver", "both"]:
        print(f'{silver = }')

    if mode not in ["gold", "both"]:
        return

    gold = silver
    # Calculate new combinations
    for line, bad_indicies in zip(data, all_bad_indicies):
        if not len(bad_indicies):
            continue

        for idx in bad_indicies:
            new_combination = line.copy()
            new_combination.pop(idx)
            if is_safe(new_combination, boolean=True):
                gold += 1
                break

    print(f'{gold = }')

if __name__ == "__main__":
    main(data_type='test')
    main(mode='both', data_type='')