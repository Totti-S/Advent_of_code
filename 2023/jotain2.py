import re
def totti_fun(string, part_value):
    left = string[:string.index('#')]
    right = string[string.rindex('#')+1:]
    static_length = string.rindex('#') - string.index('#') + 1
    minimum = min(len(left), len(right))
    left_parts = part_value - static_length
    remove_combinations = 0 if minimum > left_parts else minimum - left_parts 
    maximum_combinations = left_parts + remove_combinations + 1
    return maximum_combinations

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


def pylly(string, array):
    all_hash = re.findall(r'#+', string)
    all_questions = re.findall(r'\?+', string)
    print(all_questions)
    print(all_hash)
    hash_lens = [len(x) for x in all_hash]
    quest_lens = [len(x) for x in all_questions]
    print(hash_lens)
    
    sub_tree = []
    i = 0
    while array[0] < hash_lens[0]:
        sub_tree.append(array.pop(0))
    
    all_combinations = []
    usable_questions = +0
    print(sub_tree)
    if sub_tree:
        tmp = all_questions.pop(0)
        tmp_len = quest_lens.pop(0)
        tmp = tmp[:-1] # Remove border '?' 
        print(tmp, sub_tree, '->', end='')
        all_combinations.append(teijo_fun(tmp, sub_tree))
        print(all_combinations)
        usable_questions = tmp_len - (sum(sub_tree) + len(sub_tree))
        if usable_questions:
            quest_lens.insert(0, usable_questions)
            all_questions.insert(0, '?'*usable_questions)

    print(all_questions)
    print('string', string)
    string = ''
    for x,y in zip(all_questions, all_hash):
        string += x + y
    string += all_questions[-1]
    print('new string', string)

    hits = []
    hash_ind = string.index('#')
    i = 0
    length = array[i]

    while length >= hash_ind:
        hits.append(i)
        if i < len(all_hash):
            hash_ind += hash_lens[i] + quest_lens[i+1]
            print(hash_ind)
        else:
            break
        i += 1

    if hits:
        first_ind = quest_lens[0]
        last_ind = sum(hash_lens[:len(hits)]) + sum(quest_lens[:len(hits)])
        # if len(hits) > 1:
        #     for i,hit in enumerate(hits[0:-1],1):
        #         last_ind += hit + quest_lens[i+1]
        print(first_ind, last_ind)
        print(hits)
        length = last_ind - first_ind
        if length == array[0]:
            array.pop(0)
            new_string = string[last_ind+1:]
        else:
            new_string = string[:first_ind] + '#' * length + string[last_ind:]
        print(new_string)
if __name__ == '__main__':
    print(pylly('??????##?#?????', [1, 2, 5, 1]))