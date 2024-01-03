from collections import Counter
from utilities.get_data import get_data
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type, line_is_numbers=False)

    # print(data)
    bricks = []
    for line in data:
        start, end = line.split('~')
        s_list, e_list = start.split(','), end.split(',')
        s = [int(x) for x in s_list]
        e = [int(x) for x in e_list]
        bricks.append([s,e])

    bricks.sort(key=lambda x: x[0][2])
    
    max_x = 0
    max_y = 0
    for brick in bricks:
        for i in brick:
            if i[0] > max_x:
                max_x = i[0]
            if i[1] > max_y:
                max_y = i[1]

    array = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    top_most_brick = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    brick_supports = {
        0 : [] # Floor
    }
    for i, brick in enumerate(bricks,1):
        diff_x = brick[1][0] - brick[0][0]
        diff_y = brick[1][1] - brick[0][1]
        diff_z = brick[1][2] - brick[0][2]

        if diff_z != 0 or (diff_x == 0 and diff_y == 0 and diff_z==0): # Vertical brick
            x, y = brick[0][0], brick[0][1]
            array[y][x] += diff_z +1
            brick_supports[top_most_brick[y][x]].append(i)
            top_most_brick[y][x] = i
        else: # Horizontal brick
            x_0, y_0,_ = brick[0]
            x_1, y_1,_ = brick[1]

            if diff_y != 0: # Y-axis horizontal brick
                tmp_array = array[y_0:y_1+1]
                tmp_array = [arr[x_0] for arr in tmp_array]
                z_max = max(tmp_array)
                indices = [j for j,z in enumerate(tmp_array, y_0) if z == z_max]
                b_support = set([top_most_brick[j][x_0] for j in indices])
            else:           # X-axis horizontal brick
                tmp_array = array[y_0][x_0:x_1+1]
                z_max = max(tmp_array)
                indices = [j for j,z in enumerate(tmp_array, x_0) if z == z_max]
                b_support = set([top_most_brick[y_0][j] for j in indices])

            for b in b_support:
                brick_supports[b].append(i)

            for x in range(x_0, x_1+1):
                for y in range(y_0, y_1+1):
                    array[y][x] = z_max + 1
                    top_most_brick[y][x] = i
        brick_supports[i] = []

    supported_by = {i : 0 for i in range(1,len(bricks)+1)}
    for brick, arr in brick_supports.items():
        for b in arr:
            supported_by[b] += 1
    
    # We count firstly all the bricks that support nothing
    # Secondly we need to count the bricks that are 'reduntant' in support sense;
    # all bricks that the support brick is supporting have another brick to be supported by
    
    # For Gold solution we record the bricks
    total = 0
    no_falling = set()
    for brick, support in brick_supports.items():
        if not support:
            no_falling.add(brick)
            total += 1
            # print(brick)
            continue

        for b in support:
            if supported_by[b] == 1:
                break
        else:
            # print(brick)
            no_falling.add(brick)
            total +=1

    print(f'{mode} : {total}')

    # .....ähhhhhhh should have somehow known that the tree struct would have been better
    # Technically we have tree struct here

    def mari_got_rekt(node): # This name honors event where Mari got rekt while I was coding this solution
        if not brick_supports[node]:
            return 0
        if node in no_falling:
            return 0

        tree = {node}
        node_list = [node]
        new_node_list = []
        tmp_list = []
        left_overs = {}
        while node_list:
            brick = node_list.pop(0)
            for b in brick_supports[brick]:
                if supported_by[b] == 1:
                    tree.add(b)
                    new_node_list.append(b)
                else:
                    tmp_list.append(b)

            if not node_list:
                counter = Counter(tmp_list)
                for t, count in counter.items():
                    seen = count
                    if t in left_overs:
                        seen += left_overs[t]
                    if supported_by[t] == seen:
                        tree.add(t)
                        new_node_list.append(t)
                    else:
                        left_overs[t] = seen
                node_list = new_node_list
                tmp_list = []
        return len(tree) - 1
    
    gold = 0
    for i in range(1, len(bricks) + 1):
        gold += mari_got_rekt(i)
        print(i, gold)

    print('Gold :', gold)

if __name__ == "__main__":
    main()