from utilities.get_data import get_data
from jotain import kakka
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    def teijo_fun(array, ranget):
        if len(ranget) == 1:
            return len(array) - ranget[0] + 1
        max_length = len(array) - (ranget[0]+1) - (sum(ranget[1:]) + (len(ranget[1:])-1))
        total = 0
        for i in range(max_length+1):
            new_arr = array[ranget[0]+1+i:]
            jotain = teijo_fun(new_arr, ranget[1:])
            # print(f'{new_arr} ---> {jotain}, ranget: {ranget[1:]}')
            total += jotain
        return total
        # return int(sum([(n*(n+1))/2 for n in range(1,x+1)]))

    # Counts all possible combinations from one string group
    # with broken parts (#) inside, 
    def totti_fun(string, part_value):
        left = string[:string.index('#')]
        right = string[string.rindex('#')+1:]
        static_length = string.rindex('#') - string.index('#') + 1
        minimum = min(len(left), len(right))
        left_parts = part_value - static_length
        remove_combinations = 0 if minimum > left_parts else minimum - left_parts 
        maximum_combinations = left_parts + remove_combinations + 1
        return maximum_combinations

    # print(data)
    total = 0
    ei_loppu = []
    for i,line in enumerate(data):
        spring_row, damaged = line.split()
        damaged = damaged.split(',')
        damaged = [int(x) for x in damaged]
        # # print()
        # if i == 808:
        #     print('Alku', spring_row, damaged)
        check_if_same = ('',[])
        while check_if_same != (spring_row, damaged):
            check_if_same = (spring_row, damaged)
            spring_row = spring_row.rstrip('.').lstrip('.')
            if spring_row.startswith('#'):
                spring_row = spring_row[damaged[0]+1:]
                damaged.pop(0)
            if spring_row.endswith('#'):
                spring_row = spring_row[:(damaged[-1]+1)*-1]
                damaged.pop()
            if not damaged:
                break

            spring_rows = list(filter(None, spring_row.split('.')))
            min_damage = min(damaged)
            spring_rows = [spring_row for spring_row in spring_rows if len(spring_row) >= min_damage]
            max_damage = max(damaged)
            if damaged.count(max_damage) == 1:
                tmp_springs = [spring_row for spring_row in spring_rows if len(spring_row) >= max_damage]
                if len(tmp_springs) == 1 and len(tmp_springs[0]) == max_damage:
                    spring_rows = [spring_row for spring_row in spring_rows if len(spring_row) < max_damage]
                    damaged.pop(damaged.index(max_damage))
            if not damaged:
                break
            if damaged[0] > len(spring_rows[0]):
                spring_rows.pop(0)
            if damaged[-1] > len(spring_rows[-1]):
                spring_rows.pop()

            if len(spring_rows) > 1 and spring_rows[0].endswith("#") and damaged[0] >= len(spring_rows[0]) -1:
                spring_rows.pop(0)
                damaged.pop(0)
            if not damaged:
                break
            if len(spring_rows) > 1 and spring_rows[-1].startswith('#') and damaged[-1] >= len(spring_rows[-1]) -1:
                spring_rows.pop()
                damaged.pop()
            if not damaged:
                break
            if len(spring_rows[0]) == damaged[0] and "#" in spring_rows[0]:
                spring_rows.pop(0)
                damaged.pop(0)
            if not damaged:
                break
            if len(spring_rows[-1]) == damaged[-1] and "#" in spring_rows[-1]:
                spring_rows.pop()
                damaged.pop()
            # if not damaged:
            #     break

            
            symbols = sum([len(s) for s in spring_rows])
            springs_length = len(spring_rows)
            spring_row = ".".join(spring_rows)
            if not damaged:
                break
            if sum(damaged) == spring_row.count('#'):
                spring_row = ''
                damaged = []
                break
            if sum(damaged) == symbols:
                spring_row = ''
                damaged = []
                break
            if springs_length == 1 and sum(damaged) + len(damaged) -1 == len(spring_row):
                spring_row = ''
                damaged = []
                break
            if len(spring_row) > 2 and damaged[0] == 1 and spring_row[1] == '#':
                damaged.pop(0)
                spring_row = spring_row[2:]
            if not damaged:
                break
            if len(spring_row) > 2 and damaged[-1] == 1 and spring_row[-2] == '#':
                damaged.pop()
                spring_row = spring_row[:-2]
            if not damaged:
                break
            
            # if i == 808:
            #     print('Väli', spring_row, damaged)
            # first_value = spring_row.split('.')[0]
            # if len(damaged) > 1 and '#' in first_value and len(first_value) < sum(damaged[0:2]):
            #     combinations = totti_fun(first_value, damaged[0])

        # if i == 808:
        #     print('Loppu', spring_row, damaged)

        
        if not damaged:
            total += 1
            continue
        # Easy Special case where there is only one line and one string
        elif len(spring_row.split('.')) == 1 and len(damaged) == 1: 
            if '#' in spring_row:
                maximum_combinations = totti_fun(spring_row, damaged[0])
            else:
                maximum_combinations = len(spring_row) - damaged[0] + 1
            # print(f'{spring_row}, {damaged} -> {maximum_combinations}')
            total += maximum_combinations - 1   # compensate for adding after the loop
            spring_row = ''
            damaged = []

        elif len(damaged) == 1:
            if "#" in spring_row:
                spring_row = [x for x in spring_row.split('.') if '#' in x][0]
                maximum_combinations = totti_fun(spring_row, damaged[0])
            else:
                maximum_combinations = 0
                for spring in spring_row.split('.'):
                    maximum_combinations += len(spring) - damaged[0] + 1
            total += maximum_combinations -1
            # print(f'1. {spring_row}, {damaged} -> {maximum_combinations}')
            spring_row = ''
            damaged = []
        elif len(spring_row.split('.')) == 1 and spring_row:
            if "#" in spring_row:
                # print(f'2. {spring_row}, {damaged}')
                maximum_combinations = 0
            else:
                maximum_combinations = teijo_fun(spring_row, damaged)
                total += maximum_combinations - 1     
                spring_row = ''
                damaged = []
        elif all([dmg == 1 for dmg in damaged]):
            c = spring_row.count('#')
            spring_row = spring_row.replace('?#?','.').replace('?#','').replace('#?','')
            damaged = damaged[c:]
            # print(spring_row, damaged, '->', after, d)
            if len(damaged) == 1:
                total += spring_row.count('?')
                spring_row = ''
                damaged = []
            else:
                # print(spring_row)
                max_fit = [len(x)+1 // 2 for x in spring_row.split('.')]    # how many ones fits to group
                lenghts = [len(x) for x in spring_row.split('.')]
                counter = [0] * len(max_fit)
                valid_perms = []
                # print('max', max_fit)
                while True:
                    counter[0] += 1
                    i = 0
                    while i < len(counter):
                        if counter[i] > max_fit[i]:
                            counter[i] = 0
                            if i+1 != len(max_fit):
                                counter[i+1] += 1
                            i+=1
                            continue
                        break
                    if not any(counter):
                        break
                    # print(counter, sum(damaged))
                    if sum(counter) == sum(damaged):
                        valid_perms.append(counter.copy())
                
                # print(spring_row, damaged, '->', valid_perms)
                combinations = 0
                for valid in valid_perms:
                    partial = 1
                    for v, x in zip(valid, lenghts):
                        if v == 1:
                            partial *= x
                        elif v == 2:
                            n = x - 2
                            partial *= (n*(n+1))/2
                        elif v >= 3:
                            partial *= teijo_fun('?'*x, [1]*v)
                    combinations += partial
            # print(spring_row, damaged, '->', combinations)
            total += combinations - 1
            spring_row = ''
            damaged = []
        elif spring_row.count('#') == 0:
            # print(f'4. {spring_row}, {damaged} -> ', end='')
            combinations = kakka(spring_row, damaged)
            total += combinations - 1
            # print(combinations)
            spring_row = ''
            damaged = []
                    

        # print('Loppu', spring_row, damaged)
        if not spring_row or not damaged or (len(damaged) == 1 and len(spring_row) == damaged[0]):
            # print('Käsitelty')
            total += 1
            continue

        ei_loppu.append((spring_row, damaged, i))
    
    for ei in ei_loppu:
        print(*ei)
    print(f'Käsittelemättä vielä: {len(ei_loppu)}')

    print(f'{mode} : {total}')

if __name__ == "__main__":
    main()