from utilities.get_data import get_data
from time import perf_counter
from copy import deepcopy
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    def tilt(given_data):
        new_columns = []
        for string in given_data:
            string = ''.join(string)
            index = 0
            new_string = string
            tmp = ''
            while True:
                if '#' in new_string:
                    sqaure = new_string.index('#')
                else:
                    sqaure = len(new_string)
                rounded_rocks = new_string[index:sqaure].count('O')
                length = len(new_string[index:sqaure])
                tmp += 'O' * rounded_rocks
                tmp += '.' * (length - rounded_rocks)
                if '#' in new_string:
                    tmp += '#'
                index = sqaure + 1
                if index >= len(new_string):
                    break
                new_string = new_string[index:]
                index = 0
            new_columns.append(tmp)
        return new_columns

    def rotate(array):  # 90 degrees to clockwise rotation
        return [[array[i][j] for i in range(len(data[0]))] for j in range(len(data)-1,-1,-1)]

    by_columns = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    by_strings = tilt(by_columns)
    by_rows = [[by_strings[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    by_rows = [''.join(line) for line in by_rows]

    total = 0
    by_rows.reverse()
    for i,line in enumerate(by_rows,1):
        total += line.count('O') * i
    
    print(f'{mode} : {total}')

    ### Gold start
    columns = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    tmp = []
    cycles = 1_000_000_000
    tmp.append(columns.copy())
    for i in range(cycles):
        for _ in range(4):
            tilted = tilt(columns)
            columns = rotate(tilted)
        if columns in tmp and i < 100:
            print('found cycle', i)
            permutations = tmp[tmp.index(columns):]
            break
        tmp.append(columns.copy())
    
    cycles_left = cycles - i - 1
    cycle_end_index = cycles_left % len(permutations)
    last_position = permutations[cycle_end_index]

    by_rows = [[last_position[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    by_rows = [''.join(line) for line in by_rows]

    gold = 0
    by_rows.reverse()
    for i,line in enumerate(by_rows,1):
        gold += line.count('O') * i

    print('Gold :', gold)

if __name__ == "__main__":
    main()