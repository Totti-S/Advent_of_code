from utilities.get_data import get_data
from collections import defaultdict
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    instructions = data.pop(0)
    data.pop(0)

    nodes = {}
    for line in data:
        node, LR = line.split('=')
        LR = LR.strip().lstrip('(').rstrip(')').split(', ')
        node = node.strip()
        nodes[node] = LR

    # print(nodes)

    if mode == 'silver':
        total_moves = 0
        inst_index = 0
        position = 'AAA'
        while True:
            move = instructions[inst_index]
            index = (move == 'R')
            position = nodes[position][index]
            total_moves += 1
            inst_index += 1
            if position == 'ZZZ':
                break
            if inst_index == len(instructions):
                inst_index = 0
    else:
        total_moves = 0
        inst_index = 0
        positions = [node for node in nodes if node.endswith('A')]
        print(positions)
        loop_lengths = [15871,19637,12643, 14257, 21251, 19099]
        prime_factors = [[59, 269], [73, 269], [47, 269], [53, 269], [79, 269], [71,269]]
        primes = [59, 269, 73, 47, 53, 79, 71]
        from math import sqrt
        
        def Prime(number,itr):  #prime function to check given number prime or not
            if itr == 1:   #base condition
                return True
            if number % itr == 0:  #if given number divided by itr or not
                return False
            if Prime(number,itr-1) == False:   #Recursive function Call
                return False
                
            return True

        print([Prime(num, int(sqrt(num)+1)) for num in loop_lengths])



        # loops = [[(pos,0)] for pos in positions]
        # loop_detected = [False] * len(positions)
        # last_length = 0
        # j = 5
        # z_pos = 0
        # position = positions[j]
        # while True:
        #     move = instructions[inst_index]
        #     i = 0
        #     # while i < len(positions):
        #     #     position = positions[i]
        #     #     index = (move == 'R')
        #     #     new_position = nodes[position][index]
        #     #     # if not loop_detected[i] and new_position not in loops[i]:
        #     #     #     loops[i].append((new_position, inst_index))
        #     #     # elif (new_position, inst_index) in loops[i]:
        #     #     #     loop_detected[i] = True
        #     #     #     j = loops[i].index((new_position, inst_index))
        #     #     #     last_length = len(loops[i]) - len(loops[i][j:])
        #     #     #     loops[i] = loops[i][j:]
        #     #     #     print('moi')

        #     #     positions[i] = new_position
        #     #     i += 1
        #     index = (move == 'R')
        #     total_moves += 1
        #     inst_index += 1
        #     position = nodes[position][index]
        #     if position.endswith('Z'):

        #         print(position, total_moves, total_moves-z_pos)
        #         z_pos = total_moves
        #     if inst_index == len(instructions):
        #         inst_index = 0
        
        from math import prod 
        # if not all([pos.endswith('Z') for pos in positions]):
        total_moves = prod(primes)
        
        # print(loops)
    print(total_moves)




if __name__ == "__main__":
    # from time import perf_counter_ns
    main('gold')