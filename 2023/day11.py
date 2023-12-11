from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)
    max_rows = len(data)
    max_columns = len(data[0])


    row_counts = []
    for line in data:
        r = line.count('#')
        row_counts.append(r)

    col_counts = []
    for i in range(0,max_columns):
        col_string = "".join([x[i] for x in data])
        c = col_string.count('#')
        col_counts.append(c)
    
    silver_data = data.copy()
    i = 0
    for j, value in enumerate(row_counts):
        if not value:
            silver_data.insert(j+i,'.'*max_columns)
            i+=1
    max_rows += i

    i = 0
    for j, value in enumerate(col_counts): 
        if not value:
            k = 0
            while k < max_rows:
                silver_data[k] = silver_data[k][:j+i+1] + '.' + silver_data[k][j+i+1:]
                k += 1
            i += 1

    galaxies = []
    for i,line in enumerate(silver_data):
        alls = [j for j,x in enumerate(line) if x=='#']
        for gal in alls:
            galaxies.append((i,gal))

    silver_total = 0
    for i, galaxie in enumerate(galaxies):
        for galaxie_2 in galaxies[i+1:]:
            silver_total += abs(galaxie_2[0] - galaxie[0]) + abs(galaxie_2[1] - galaxie[1])
    print(f'Silver : {silver_total}')

    col_expanding = [not c for c in col_counts]
    row_expanding = [not r for r in row_counts]

    space_inc = 999_999

    galaxies = []
    for i,line in enumerate(data):
        alls = [j for j,x in enumerate(line) if x=='#']
        for gal in alls:
            galaxies.append((i,gal))
    total = 0
    for i, galaxie in enumerate(galaxies):
        for galaxie_2 in galaxies[i+1:]:
            r_1, c_1 = galaxie
            r_2, c_2 = galaxie_2
            row_expansion = sum(row_expanding[r_1+1:r_2])
            col_expansion = sum(col_expanding[c_1+1:c_2] if c_1 < c_2 else col_expanding[c_2+1:c_1])
            total += abs(galaxie_2[0] - galaxie[0]) + abs(galaxie_2[1] - galaxie[1])
            total += (row_expansion + col_expansion) * space_inc

    print(f'Gold : {total}')

if __name__ == "__main__":
    main()