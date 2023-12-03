from utilities.get_data import get_data, str_number_to_int
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    data = str_number_to_int(data)
    # Solution: Go through line by line and char by char, when char is integer sequence
    #           record start and end index of it. Use these indecies to 'scan' for symbols
    #           that are touching the number. First check the column before start index,
    #           then the indicies between start and end, and then column after end.
    #
    # Gold:     If the symbol we find is * then record the number in dictionary using 
    #           row and col as key. Accept only list that has two entries

    gears = defaultdict(list)
    def check_for_symbol(r, c, num):
        if data[r][c] == "*":
            gears[(r,c)].append(num)
        return data[r][c] != '.'
    
    total, gear_sum = 0, 0
    for row, line in enumerate(data):
        number = None
        def scan(column, middle=False):
            if row != 0:
                if check_for_symbol(row-1, column, number): 
                    return True
            if not middle:
                if check_for_symbol(row, column, number): 
                    return True
            if row + 1 != len(data):
                if check_for_symbol(row+1, column, number): 
                    return True
            return False

        start, end = None, None
        for col, char in enumerate(line):
            if start is not None and end is not None:
                start, end = None, None
            if type(char) == int:
                if start is None:
                    start = col
                if col+1 != len(line) and type(line[col+1]) == int:
                    continue
                end = col
                number = int("".join([str(line[x]) for x in range(start,end+1)]))
                
                # check start
                if start != 0 and scan(start-1): 
                    total += number
                    continue

                # check middle
                middle_check = False
                for k in range(start, end+1):
                    middle_check = scan(k, True)
                    if middle_check: break
                if middle_check: 
                    total += number
                    continue

                # check end
                if end+1 != len(line) and scan(end+1): 
                    total += number

    print(total) # Silver
    
    from math import prod
    for gear in gears.values():
        if len(gear) == 2:
            gear_sum += prod(gear)
    print(gear_sum) # Gold

if __name__ == "__main__":
    main()