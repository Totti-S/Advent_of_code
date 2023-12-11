from utilities.get_data import get_data
from operator import sub  # I use this to do tuple math with maps 
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    row_expanding = [not line.count('#') for line in data]
    col_expanding = [not "".join([x[i] for x in data]).count('#') for i in range(0, len(data[0]))]

    galaxies = []
    for i,line in enumerate(data):
        alls = [j for j,x in enumerate(line) if x=='#']
        for gal in alls:
            galaxies.append((i,gal))

    def count_shortest_path(space_increase):
        total = 0
        for i, (r_1, c_1) in enumerate(galaxies):
            for (r_2, c_2) in galaxies[i+1:]:
                row_expansion = sum(row_expanding[r_1+1:r_2])
                col_expansion = sum(col_expanding[c_1+1:c_2] if c_1 < c_2 else col_expanding[c_2+1:c_1])
                total += abs(r_1-r_2) + abs(c_1-c_2) + (row_expansion + col_expansion) * space_increase
        return total
    
    silver = count_shortest_path(1)
    gold = count_shortest_path(999_999)
    print(f'Silver : {silver}')
    print(f'Gold : {gold}')

if __name__ == "__main__":
    main()