import itertools
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


def kakka(string, array):
    string_arr = string.split('.')

    perm_groups = []
    for s_arr in string_arr:
        jotain = [None]
        for j, a in enumerate(array):
            if a <= len(s_arr):
                jotain.append(j)
        perm_groups.append(jotain)
    # print(perm_groups)

    for i in range(len(string_arr)):
        count = 0
        for group in perm_groups:
            if i in group:
                count +=1
            if count >= 2:
                break
        else:
            if count == 1:
                k = 0
                while True:
                    group = perm_groups[k]
                    if i in group:
                        all_uniques = set()
                        new_group = []
                        new_sum = 0
                        # print(group, i)
                        # print(list(reversed(group)))
                        r = list(reversed(group))
                        for j in r[r.index(i):]: # Look left

                            if j is None:continue
                            if len(string_arr[k]) - (new_sum + len(new_group)) >= array[j]:
                                new_sum += array[j]
                                new_group.append(j)
                        all_uniques.update(new_group)
                        new_group = []
                        new_sum = 0
                        for j in group[group.index(i):]: # Look right
                            if len(string_arr[k]) - (new_sum + len(new_group)) >= array[j]:
                                new_sum += array[j]
                                new_group.append(j)
                            else:
                                break
                        all_uniques.update(new_group)
                        # print(all_uniques)
                        perm_groups[k] = list(all_uniques)
                        break
                    k += 1

            elif count == 0:
                pass
            #     print('jotain meni vikaan')

    # print(perm_groups)
    for i,group in enumerate(perm_groups):
        if len(group) == 1:
            # print(group)
            unique_val = group[0]
            j = 0
            while j < i:  #left side
                k = 0
                while k < len(perm_groups[j]):
                    val = perm_groups[j][k]
                    if val is None:
                        k +=1
                        continue
                    if val >= unique_val:
                        del perm_groups[j][k]
                        k -= 1
                    k += 1
                j += 1
            
            j = i+1
            while j < len(perm_groups):
                k = 0
                while k < len(perm_groups[j]):
                    val = perm_groups[j][k]
                    if val is None:
                        k +=1
                        continue
                    if val <= unique_val:
                        del perm_groups[j][k]
                        k -= 1
                    k += 1
                j += 1
    # print(perm_groups)
    all_groups = []
    for i,group in enumerate(perm_groups): 
        new_group = []
        for L in range(len(group) + 1):
            for subset in itertools.combinations(group, L):
                new_group.append(subset)
        # print('before', group, '->', new_group)
        new_group = list(filter(lambda x: len(x) == 1 or None not in x, new_group))
        new_group = list(filter(lambda x: x, new_group))
        new_group = list(filter(lambda x: sum([array[h] if h is not None else 0 for h in x]) + (len(x)-1) <= len(string_arr[i]), new_group))
        # print(group, '->', new_group)
        all_groups.append(new_group)
    
    def filder(x):
        flatten_list= [item for row in x for item in row ]
        flatten_list_wo_none = [item for item in flatten_list if item is not None]
        # print(x, '->', flatten_list_wo_none, flatten_list_wo_none == list(range(len(array))), list(range(len(array))))
        return flatten_list_wo_none == list(range(len(array)))
    # print(all_groups)
    all_combinations = itertools.product(*all_groups)
    # for c in all_combinations: print(c)
    all_combinations = filter(filder, all_combinations)
    
    total = 0
    combos = []
    for combination in all_combinations:
        combos.append(combination)
        subset = 1
        for i,x in enumerate(combination):
            if len(x) == 1 and x[0] is None:continue
            arr = [array[val] for val in x]
            subset *= teijo_fun(string_arr[i], arr)
            # print(combination, subset)
        total += subset
    # print('all_combinations')
    # for c in combos: print(c)
    # print('total', total)
    return total
if __name__ == '__main__':
    # kakka('????.??.??.??',[3, 1, 2, 1] )
    # kakka('?????.?.?.????', [3, 2, 1])
    print(kakka('?.???????.?', [1, 4, 2, 1]))