from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)


    seeds = [int(tmp) for tmp in data[0].split(':')[1].split()]
    data.pop(0)
    data.pop(0)
    print(data)
    groups = []
    i = -1
    for line in data:
        if line.endswith('map:'): 
            groups.append([])
            i +=1
            continue
        if line != '':
            groups[i].append([int(tmp) for tmp in line.split()])

    if mode == 'silver':

        lowest = None
        type_index = None
        for seed in seeds:
            type_index = seed
            for group in groups:
                for nums in group:
                    dest, sour, r = nums
                    if sour <= type_index <= sour + r:
                        delta  = type_index - sour
                        type_index = delta + dest
                        break
            if lowest is None or type_index < lowest:
                lowest = type_index

    else:
        ultimate_filter = []
        for i in range(0, len(seeds),2):
            ultimate_filter.append([seeds[i], seeds[i], seeds[i+1]])
        
        g = 0
        while g < len(groups):
            group = groups[g]
            new_ultimate = []
            s = 0
            while s < len(ultimate_filter):
                dest, source, length = ultimate_filter[s]
                a = dest
                b = dest + length -1

                i = 0
                while i < len(group):
                    dest_2, source_2, length_2 = group[i]
                    x = source_2
                    y = source_2 + length_2 - 1
                    offset = dest_2 - source_2
                    if b < x or y < a:
                        i += 1
                        continue
                    else:
                        filter = [0,0,0]
                        if a <= x and b >= y:
                            # print('Aikaisemmin täällä')
                            filter = [dest_2, source + (x-a), length_2]
                            if x != a:
                                ultimate_filter.append([dest, source, x-a])         # left side
                            if b != y:
                                ultimate_filter.append([dest + (y-a+1), source + (y-a+1), b-y])    # right side
                        elif x <= a and b <= y: # Seed inside
                            filter = [dest + offset, source, length]
                            if x != a:
                                group.append([dest_2, source_2, a-x])      # left side
                            if b != y:
                                group.append([dest_2 + (b-x+1), source_2 + (b-x+1), y-b]) # right side
                            
                        elif x < a:  # Crossing left side
                            filter = [dest + offset, source, (y-a+1)]
                            group.append([dest_2, source_2, a-x])
                            ultimate_filter.append([dest + (y-a+1), source +(y-a+1), b-y])
                        else:   # Seed crossing right side
                            filter = [dest_2, source + (x-a), (b-x+1)]
                            group.append([dest_2 + (b-x+1), source_2 + (b-x+1), (y-b)])
                            ultimate_filter.append([dest, source, (x-a)])
                        new_ultimate.append(filter)
                        group.pop(i)
                        ultimate_filter.pop(s)
                        s += -1
                    break
                s += 1
            
            ultimate_filter += new_ultimate
            g +=1

        ultimate_filter.sort(key=lambda x: x[0])
        lowest = ultimate_filter[0][0]

    print(f'lowest {lowest}')


if __name__ == "__main__":
    main('gold', data_type='test')
    # main('gold')