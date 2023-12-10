from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    North = (-1,0)
    East = (0,1)
    South = (1,0)
    West = (0,-1)

    columns = len(data[0])
    rows = len(data)
    S_x, S_y = None, None
    for i,line in enumerate(data):
        if 'S' in line:
            S_x, S_y= line.index('S'), i 
            S_y = i

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
        South : '|LXJS', # v
        East : '7-JXS', # >
        North : 'XF|7S', # ^
        West : 'FXL-S' # <
    }
    transformation = {
        0: South,
        1: East,
        2: North,
        3: West,
        4: None # Starting position
    }
    
    found_loops = []
    for direction in directions:
        found_loop = False
        current_pos = (S_y, S_x)
        maybe_loop = []
        next_pos = direction
        while True:
            next_dir = (next_pos[0]-current_pos[0], next_pos[1]-current_pos[1])
            y,x = next_pos
            next_symbol = data[y][x]
            if next_symbol in acceptable_symbols[next_dir]:
                maybe_loop.append(next_pos)
                trans = acceptable_symbols[next_dir].index(next_symbol)
                tmp = transformation[trans]
                if tmp is None:
                    found_loop = True
                    break
                current_pos = next_pos
                next_pos = (next_pos[0]+tmp[0],next_pos[1]+tmp[1])
                continue
            break

        if found_loop:
            found_loops.append(maybe_loop)

    main_loop = found_loops[0]
    farthest_point = int(len(main_loop)/2)
    print(f'Silver : {farthest_point}')

    
    # Find handness of the loop (Rotation direction):
    current_location = (S_y, S_x)
    turn = ''
    for location in main_loop:
        direction = (location[0] - current_location[0], location[1]-current_location[1])
        y,x = location
        next_symbol = data[y][x]
        if next_symbol == 'S': break
        elif next_symbol not in '-|':
            if direction == East:
                turn += 'R' if next_symbol == '7' else 'L'
            elif direction == West:
                turn += 'R' if next_symbol == 'L' else 'L'
            elif direction == South:
                turn += 'R' if next_symbol == 'J' else 'L'
            elif direction == North:
                turn += 'R' if next_symbol == 'F' else 'L'
        
        current_location = location

    handness = 'L' if turn.count('L') > turn.count('R') else 'R'
    
    # Replace S with pipe pieace
    last_pipe = main_loop[-2]
    first_pipe = main_loop[0]
    difference = (last_pipe[0]-first_pipe[0], last_pipe[1] - first_pipe[1])

    match difference:
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

    # We go pipes in the loop piece by piece scanning through tiles
    # that are located inside loop. We use 'handness' to represent the
    # clock-wise or counter clock-wise rotation of loop. Using that knowledge
    # we can determine which tiles are inside of the loop

    tiles = set()
    current_location = (S_y, S_x)
    for location in main_loop:
        direction = (location[0] - current_location[0], location[1] - current_location[1])

        y,x = location
        pipe = data[y][x]
        match (pipe):
            case '-':
                if handness == 'R':
                    check_dir = [South] if direction[1] == 1 else [North]
                else:
                    check_dir = [North] if direction[1] == 1 else [South]
            case '|':
                if handness == 'R':
                    check_dir = [West] if direction[0] == 1 else [East]
                else:
                    check_dir = [East] if direction[0] == 1 else [West]
            case 'F':
                if handness == 'R' and direction == North or handness == 'L' and direction == West:
                    current_location = location
                    continue
                check_dir = [North, West]     
            case 'L':
                if handness == 'R' and direction == West or handness == 'L' and direction == South:
                    current_location = location
                    continue
                check_dir = [South, West]   
            case '7':
                if handness == 'R' and direction == East or handness == 'L' and direction == North:
                    current_location = location
                    continue
                check_dir = [North, East]
            case 'J':
                if handness == 'R' and direction == South or handness == 'L' and direction == East:
                    current_location = location
                    continue
                check_dir = [South, East]
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
                if tmp_location in main_loop:
                    break
                tiles.add(tmp_location)

        current_location = location

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