from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    # print(data)
    total = 0
    for line in data:
        spring_row, damaged = line.split()
        damaged = damaged.split(',')
        damaged = [int(x) for x in damaged]
        print()
        print('Alku', spring_row, damaged)
        while spring_row.endswith('#') or spring_row.startswith('#') or spring_row.startswith('.') or spring_row.endswith('.'):
            if spring_row.startswith('#'):
                spring_row = spring_row[damaged[0]+1:]
                damaged.pop(0)
            if spring_row.endswith('#'):
                spring_row = spring_row[:(damaged[-1]+1)*-1]
                damaged.pop()
            if spring_row.startswith('.'):
                spring_row = spring_row[1:]
            if spring_row.endswith('.'):
                spring_row = spring_row[:-1]

        print('Loppu', spring_row, damaged)
        if not spring_row or not damaged or (len(damaged) == 1 and len(spring_row) == damaged[0]):
            total += 1
            continue
        
        spring_rows = list(filter(None, spring_row.split('.')))
        min_damage = min(damaged)
        spring_rows = [spring_row for spring_row in spring_rows if len(spring_row)>= min_damage]

        # i = 0
        # for spring in spring_row:
        #     total_2 = 1
        #     # print(spring_row, damaged)
        #     if spring.count('#') == damaged[i]:
        #         i += 1
        #         total_2 *= 1
        #         continue
        #     elif len(spring) - 1 == damaged[i]:
        #         i += 1
        #         total_2 *= 2
        #         continue
        #     elif len(spring) > damaged[i]+1:
        #         pass
                
        #     else:
        #         assert True, f'Dont come here {spring}, {i}, {damaged[i]}'
        #     i+=1
        #     # print(total_2)
        # total += total_2
        # # print(total_2)
    
    print(f'{mode} : {total}')

if __name__ == "__main__":
    main()