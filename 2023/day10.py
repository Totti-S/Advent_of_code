from collections import defaultdict, Counter
from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    # print(data)
    columns = len(data[0])
    rows = len(data)
    # First find S
    S_x = None
    S_y = None
    for i,line in enumerate(data):
        if 'S' in line:
            S_x = line.index('S')
            S_y = i
            break

    print(S_x, S_y)
    directions = []
    if S_x != 0:
        if data[S_y][S_x-1] != '.':
            directions.append((S_y, S_x-1))
    if S_x != columns:
        if data[S_y][S_x+1] != '.':
            directions.append((S_y,S_x+1))
    if S_x != 0:
        if data[S_x-1][S_x] != '.':
            directions.append((S_y-1,S_x))
    if S_y != rows:
        if data[S_y+1][S_x] != '.':
            directions.append((S_y+1,S_x))

    acceptable_symbols = {
        (1,0) : '|LXJS', # v
        (0,1) : '7-JXS', # >
        (-1,0) : 'XF|7S', # ^
        (0,-1) : 'FXL-S' # <
    }
    transformation = {
        0: (1,0),
        1: (0,1),
        2: (-1,0),
        3: (0,-1),
        4: None 
    }
    
    # print(directions)
    found_loops = []
    for direction in directions:
        # print('moi')
        found_loop = False
        current_pos = (S_y, S_x)
        maybe_loop = []
        stack = [direction]
        while stack:
            next_pos = stack.pop(0)
            next_dir = (next_pos[0]-current_pos[0], next_pos[1]-current_pos[1])
            y,x = next_pos
            next_symbol = data[y][x]
            # print(next_pos, next_symbol)
            if next_symbol in acceptable_symbols[next_dir]:
                maybe_loop.append(next_pos)
                trans = acceptable_symbols[next_dir].index(next_symbol)
                tmp = transformation[trans]
                if tmp is None:
                    found_loop = True
                    break
                current_pos = next_pos
                stack.append((next_pos[0]+tmp[0],next_pos[1]+tmp[1]))

        if found_loop:
            found_loops.append(maybe_loop)

    # print(found_loops)

    max_len = 0
    for loop in found_loops:
        length = len(loop)
        far_poin = int(length / 2)
        max_len = far_poin if max_len < far_poin else max_len

    print(f'Silver : {max_len}')

    main_loop = found_loops.pop(0)
    # print(main_loop)

    pipe_1 = main_loop[-2]
    pipe_2 = main_loop[0]
    jotain = (pipe_1[0]-pipe_2[0], pipe_1[1] - pipe_2[1])
    # print(jotain)
    
    # find handness of the loop:
    loc = (S_y, S_x)
    turn = ''
    for location in main_loop:
        # print('location',loc)
        dir = (location[0] - loc[0], location[1]-loc[1])
        # print('direction', dir)
        y,x = location
        next_symbol = data[y][x]
        if next_symbol == 'S': break
        elif next_symbol not in '-|':
            match (dir):
                case (0,1): # -> 
                    turn += 'R' if next_symbol == '7' else 'L'
                case (0,-1): # <-
                    turn += 'R' if next_symbol == 'L' else 'L'
                case (1,0): # v
                    turn += 'R' if next_symbol == 'J' else 'L' 
                case (-1,0):
                    turn += 'R' if next_symbol == 'F' else 'L'
        # else: 
            # print('symbol', next_symbol)

        loc = location

    R_count = turn.count('R')
    L_count = turn.count('L')
    # print(turn)
    if L_count > R_count:
        handness = 'L'
    elif L_count < R_count:
        handness = 'R'
    else:
        assert True, 'Dont come here LR'
    
    # print(handness)

    match (jotain):
        case (0,2) | (0,-2):
            sym = '-'
        case (2,0) | (-2,0):
            sym = '|'
        case (1,1):
            sym = 'L'
        case (1,-1):
            sym = "J"
        case (-1,1):
            sym = "F"
        case (-1,-1):
            sym = "7"
    data[S_y] = data[S_y].replace('S', sym)
    print(sym)

    tiles = set()
    loc = (S_y, S_x)
    for location in main_loop:
        dir = (location[0] - loc[0], location[1]-loc[1])

        y,x = location
        pipe = data[y][x]
        match (pipe):
            case '-':
                if handness == 'R':
                    check_dir = [(1,0)] if dir[1] == 1 else [(-1,0)]
                else:
                    check_dir = [(-1,0)] if dir[1] == 1 else [(1,0)]
            case '|':
                if handness == 'R':
                    check_dir = [(0,-1)] if dir[0] == 1 else [(0,1)]
                else:
                    check_dir = [(0,1)] if dir[0] == 1 else [(0,-1)]
            case 'F':
                if handness == 'R' and dir == (-1,0):
                    loc = location
                    continue
                if handness == 'L' and dir == (0,-1):
                    loc = location
                    continue
                check_dir = [(-1,0), (0,-1)]     
            case 'L':
                if handness == 'R' and dir == (0,-1):
                    loc = location
                    continue
                if handness == 'L' and dir == (1,0): 
                    loc = location
                    continue          
                check_dir = [(1,0), (0,-1)]   
            case '7':
                if handness == 'R' and dir == (0,1):
                    loc = location
                    continue
                if handness == 'L' and dir == (-1,0):
                    loc = location
                    continue
                check_dir = [(-1,0), (0,1)]
            case 'J':
                if handness == 'R' and dir == (1,0):
                    loc = location
                    continue
                if handness == 'L' and dir == (0,1):
                    loc = location
                    continue
                check_dir = [(1,0), (0,1)]
            case _:
                assert False, f'Dont come here {pipe}' 
        
        for op in check_dir:
            tmp_location = location
            while True:
                tmp_location = (tmp_location[0] + op[0], tmp_location[1] + op[1])
                if tmp_location[0] < 0 or tmp_location[0] == rows:
                    break
                if tmp_location[1] < 0 or tmp_location[1] == columns:
                    break
                y,x = tmp_location
                if tmp_location in main_loop:
                    break
                
                if tmp_location == (0,6):
                    print(location, tmp_location)

                tiles.add(tmp_location)

        loc = location

    # print(f'Counts {tiles}')
    total = len(tiles)

    # tiles = list(tiles)
    # for tile in tiles:
    #     y,x = tile
    #     line = [x for x in data[y]]
    #     line[x] = '#'
    #     data[y] = "".join(line)
    
    # with open('tmp.txt', 'w') as f:
    #     f.writelines(line + '\n' for line in data)

    print('Gold:', total)

if __name__ == "__main__":
    main()