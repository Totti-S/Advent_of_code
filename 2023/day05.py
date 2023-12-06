from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)


    seeds = [int(tmp) for tmp in data[0].split(':')[1].split()]
    data.pop(0)
    data.pop(0)
    # print(data)
    regions = []
    i = -1
    for line in data:
        if line.endswith('map:'): 
            regions.append([])
            i +=1
            continue
        if line != '':
            regions[i].append([int(tmp) for tmp in line.split()])

    if mode == 'silver':

        lowest = None
        for seed in seeds:
            value = seed
            for region in regions:
                for sub_region in region:
                    dest, source, length = sub_region 
                    if source <= value <= source + length:
                        value = dest + (value-source)
                        break
            if lowest is None or value < lowest:
                lowest = value

    else:
        seed_to_region = []
        for i in range(0, len(seeds),2):
            seed_to_region.append([seeds[i], seeds[i], seeds[i+1]])
        
        g = 0
        while g < len(regions):
            region = regions[g]
            new_region = []
            
            s = 0
            while s < len(seed_to_region):
                dest, source, length = seed_to_region[s]
                a = dest
                b = dest + length -1

                i = 0
                while i < len(region):
                    dest_2, source_2, length_2 = region[i]
                    x = source_2
                    y = source_2 + length_2 - 1
                    offset = dest_2 - source_2
                    if b < x or y < a:  # Region is outside
                        i += 1
                        continue
                    else:
                        if a <= x and b >= y: # Region is same, Right side or Left side larger or Both
                            overlapping = [dest_2, source + (x-a), length_2]
                            if x != a:
                                seed_to_region.append([dest, source, x-a])
                            if b != y:
                                seed_to_region.append([dest + (y-a+1), source + (y-a+1), b-y])
                        
                        elif a >= x and b <= y: # Region inside or Inside and one side is Same
                            overlapping = [dest + offset, source, length]
                            if x != a:
                                region.append([dest_2, source_2, a-x])
                            if b != y:
                                region.append([dest_2 + (b-x+1), source_2 + (b-x+1), y-b])
                            
                        elif a > x:  # Regions Right side is inside and left is out
                            overlapping = [dest + offset, source, (y-a+1)]
                            region.append([dest_2, source_2, a-x])
                            seed_to_region.append([dest + (y-a+1), source +(y-a+1), b-y])
                        
                        else:  # Regions Left side is inside and right is out
                            overlapping = [dest_2, source + (x-a), (b-x+1)]
                            region.append([dest_2 + (b-x+1), source_2 + (b-x+1), (y-b)])
                            seed_to_region.append([dest, source, (x-a)])
                        new_region.append(overlapping)
                        region.pop(i)
                        seed_to_region.pop(s)
                        s += -1
                    break
                s += 1
            
            seed_to_region += new_region
            g +=1

        seed_to_region.sort(key=lambda x: x[0])
        lowest = seed_to_region[0][0]

    print(f'lowest {lowest}')


if __name__ == "__main__":
    # main('gold', data_type='test')
    main('gold')