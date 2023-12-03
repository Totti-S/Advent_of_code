from utilities.get_data import get_data, str_number_to_int
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)
    data = str_number_to_int(data)
    gears = defaultdict(list)
    def check_for_symbol(s,e, val, num):
        if data[s][e] == "*":
            gears[(s,e)].append(num)
        return True if data[s][e] != '.' else val
    
    total = 0
    gear_sum = 0
    for i, line in enumerate(data):
        is_near_symbol = False
        start, end = None, None
        number = None
        for j, char in enumerate(line):
            if type(char) == int:
                if start is not None:
                    if j+1 != len(line) and type(line[j+1]) == int:
                        continue
                    end = j
                else:
                    start = j
                    if j+1 != len(line) and type(line[j+1]) == int:
                        continue
                    else:
                        end = j
                number = int("".join([str(line[x]) for x in range(start,end+1)]))
                # check start if not j == 0
                if start != 0:
                    if i != 0:
                        is_near_symbol = check_for_symbol(i-1, start-1, is_near_symbol, number)
                    is_near_symbol = check_for_symbol(i, start-1, is_near_symbol, number)
                    if i+1 != len(data):
                        is_near_symbol = check_for_symbol(i+1, start-1, is_near_symbol, number)
                if is_near_symbol: 
                    total += number
                    start, end = None, None
                    is_near_symbol = False
                    continue

                # check middle
                for k in range(start, end+1):
                    if i != 0:
                        is_near_symbol = check_for_symbol(i-1, k, is_near_symbol, number)
                    if i+1 != len(data):
                        is_near_symbol = check_for_symbol(i+1, k, is_near_symbol, number)
                    if is_near_symbol: break
                if is_near_symbol: 
                    total += number
                    start, end = None, None
                    is_near_symbol = False
                    continue

                # check end if not j at the end
                if end+1 != len(line):
                    if i != 0:
                        is_near_symbol = check_for_symbol(i-1, end+1, is_near_symbol, number)
                    is_near_symbol = check_for_symbol(i, end+1, is_near_symbol, number)
                    if i+1 != len(data):
                        is_near_symbol = check_for_symbol(i+1, end+1, is_near_symbol, number)
                if is_near_symbol: 
                    total += number
                start, end = None, None
                is_near_symbol = False
    print(total) # Silver
    
    from math import prod
    for gear in gears.values():
        if len(gear) == 2:
            gear_sum += prod(gear)
    print(gear_sum)

if __name__ == "__main__":
    main()