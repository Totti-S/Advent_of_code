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
    # After completion: Instead of column by column -> row by row
    # Inspiration credit: https://github.com/PauliAnt/advent_of_code/blob/main/day3/day3.ipynb

    gears = defaultdict(list)  
    total, gear_sum = 0, 0
    for row, line in enumerate(data):
        number = None
        start, end = None, None
        for col, char in enumerate(line):
            if start is not None and end is not None: # Reset after number
                start, end = None, None
            if type(char) == int:
                if start is None:
                    start = col
                if col+1 != len(line) and type(line[col+1]) == int:
                    continue
                end = col
                number = int("".join([str(line[x]) for x in range(start,end+1)]))

                middle_range = [] # Middle row -> check start and end (if not at the border) 
                if start - 1 >= 0:
                    middle_range.append(start-1)
                if end + 1 < len(line):
                    middle_range.append(end+1)

                symbol_found = False
                for row_i in range(max(0,row-1), min(len(data), row+2)):
                    interate_over = middle_range if row_i == row else range(max(0, start-1), min(len(line), end+2))
                    for col_i in interate_over:
                        if data[row_i][col_i] == "*":
                            gears[(row_i,col_i)].append(number)
                        if data[row_i][col_i] != '.':
                            total += number
                            symbol_found = True
                            break
                    if symbol_found: break

    print(total) # Silver
    
    for gear in gears.values():
        if len(gear) == 2:
            gear_sum += gear[0] * gear[1]
    print(gear_sum) # Gold

if __name__ == "__main__":
    main()