from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    max_row = len(data)
    max_col = len(data[0])

    print(data)
    # First find the starting position
    Os_positions = []
    for i, line in enumerate(data):
        if "S" in line:
            Os_positions.append((i, line.index("S")))
    
    # Replace the starting position with a dot
    i = Os_positions[0][0]
    data[i] = data[i].replace('S','.')
    
    visited = set()
    even_number_plots = set([Os_positions[0]])
    steps = 64

    for step in range(1, steps+1):
        step_is_odd = step % 2
        new_positions = []
        while Os_positions:
            i,j = Os_positions.pop()
            visited.add((i,j))
            if i+1 < max_row and data[i+1][j] == '.':
                new_pos = (i+1,j)
                if new_pos not in visited and new_pos not in new_positions:
                    new_positions.append(new_pos)
                    if not step_is_odd:
                        even_number_plots.add(new_pos)
            if i-1 >= 0 and data[i-1][j] == '.':
                new_pos = (i-1,j)
                if new_pos not in visited and new_pos not in new_positions:
                    new_positions.append(new_pos)
                    if not step_is_odd:
                        even_number_plots.add(new_pos)
            if j+1 < max_col and data[i][j+1] == '.':
                new_pos = (i,j+1)
                if new_pos not in visited and new_pos not in new_positions:
                    new_positions.append(new_pos)
                    if not step_is_odd:
                        even_number_plots.add(new_pos)
            if j-1 >= 0 and data[i][j-1] == '.':
                new_pos = (i,j-1)
                if new_pos not in visited and new_pos not in new_positions:
                    new_positions.append(new_pos)
                    if not step_is_odd:
                        even_number_plots.add(new_pos)
        Os_positions = new_positions
        print(step, f'{round(len(visited)/(max_col*max_row),1)} %')
    
    # print(visited)
    # print()
    # print(Os_positions)
    # print()
    # print(even_number_plots)
    # print()
    total = len(even_number_plots)
    print(f'{mode} : {total}')
        

if __name__ == "__main__":
    main()