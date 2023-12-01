from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    # Solution: Go to first char that is a number. Check for string before the first 
    #           found number for potential spelled number, if yes use that instead as a solution
    #           Do only once for forward and backwards sides. Use filpped number 'names' 
    #           for backwards comparison.

    # Silver is only for numbers -> use mode varible to switch

    def convert_to_number(value:str, reverse:bool) -> str | None:
        numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        num_index = None
        found_number = None
        for i, n in enumerate(numbers,1):
            n = n[::-1] if reverse else n
            if n in value:
                found_index = value.index(n)
                if num_index is None or found_index < num_index: # Keep only the earliest seen number
                    num_index = found_index
                    found_number = str(i)
        return found_number
    

    def go_through_line(line: str, reverse: bool) -> int:
        for i, chr in enumerate(line):
            if chr.isnumeric():
                if mode == 'gold':
                    string_number = convert_to_number(line[:i], reverse)
                    if string_number is not None:
                        chr = string_number
                return int(chr)
        else:
            # This is for the 2. test case where there is no number in the string
            # Real data contains at least one number
            string_number = convert_to_number(line, reverse)
            if string_number is not None:
                chr = string_number
            return int(chr)

    calibration_sum = 0
    for line in data:
        first = go_through_line(line, False) # Forwards
        last = go_through_line(line[::-1], True) # Backwards
        calibration_sum += first *10 + last

    print(calibration_sum) # Result

def regex_solution(mode='silver', data_type=''):
    import re
    data = get_data(__file__, data_type)
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    pattern = r'(?=([1-9]|' + '|'.join(numbers) + '))' if mode == 'gold' else r'[1-9]'
    total = 0
    for line in data:
        calibration_number = ''
        all_numbers = re.findall(pattern, line)
        for num in [0, -1]:
            number = all_numbers[num]
            calibration_number += str(numbers.index(number)+1) if number in numbers else number
        total += int(calibration_number)
    print(total)

if __name__ == "__main__":
    # main('silver', 'big')
    # main('gold', 'big')
    regex_solution()
    regex_solution('gold')