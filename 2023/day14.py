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

    def transformation(array):  # 90 degrees to clockwise rotation
        return [[array[i][j] for i in range(len(data[0]))] for j in range(len(data)-1,-1,-1)]

    def print_columns(columns):
        by_rows = [[columns[i][j] for i in range(len(data))] for j in range(len(data[0]))]
        by_rows = [''.join(line) for line in by_rows]
        print('\n'.join(by_rows))
        print()

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
    s = perf_counter()
    found = False
    index = 0
    tmp.append(columns.copy())
    for i in range(cycles):
        for j in range(4):
            # if i < 2:
            #     print(i, j)
            #     print('columns')
            #     print_columns(columns)
            tilted = tilt(columns)
            columns = transformation(tilted)
            # if i < 2:
            #     print('tilted')
            #     print_columns(tilted)
        if not found and columns in tmp and i < 100:
            found = True
            print('found cycle', i)
            index = i
            permutations = tmp[tmp.index(columns):]
            break
        elif not found:
            tmp.append(columns.copy())
        # elif found and columns in tmp:
        #     print('Found cycle', i, tmp.index(columns))
    
    cycles_left = cycles - index - 1

    correct_index = cycles_left % len(permutations)
    position = permutations[correct_index]





    # # by_rows = [[north_tilted[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    # # by_rows = [''.join(line) for line in by_rows]
    
    # # print('\n'.join(by_rows))

    # rotated = [[north_tilted[j][i] for i in range(len(data))] for j in range(len(data[0]))]
    # # rotated = [list(reversed(line) for line in rotated]

    # # by_rows = [[rotated[i][j] for i in range(len(data)-1,-1,-1)] for j in range(len(data[0]))]
    # # by_rows = [''.join(line) for line in by_rows]
    # # print('jälkeen:')
    # # print('\n'.join(by_rows))
    
    # by_columns = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]

    by_rows = [[position[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    by_rows = [''.join(line) for line in by_rows]

    gold = 0
    by_rows.reverse()
    for i,line in enumerate(by_rows,1):
        gold += line.count('O') * i

    print('Gold :', gold)

if __name__ == "__main__":
    main()