from utilities.get_data import get_data
import re
from math import sqrt, prod
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    instructions = data.pop(0)
    data.pop(0)

    nodes = {}
    for line in data:
        node, L, R = re.findall(r'\w\w\w', line)
        nodes[node] = (L,R)
    
    inst_index = 0
    total_moves = 0
    if mode == 'silver':
        position = 'AAA'
        while True:
            move = instructions[inst_index]
            position = nodes[position][(move == 'R')]   # NOTE Boolean operation:
            total_moves += 1                            # False -> Left, True -> Right
            inst_index += 1
            if position == 'ZZZ':
                break
            if inst_index == len(instructions):
                inst_index = 0
    else:
        starting_positions = [node for node in nodes if node.endswith('A')]
        loop_lengths = [None] * len(starting_positions)

        for i, position in enumerate(starting_positions):
            inst_index = 0
            total_moves = 0
            end_point_found = False
            while True:
                move = instructions[inst_index]
                position = nodes[position][(move == 'R')]   # NOTE Boolean operation:
                if position.endswith('Z'):                  # False -> Left, True -> Right
                    if end_point_found:
                        loop_lengths[i] = total_moves - loop_lengths[i]
                        break
                    end_point_found = True
                    loop_lengths[i] = total_moves

                total_moves += 1
                inst_index += 1
                if inst_index == len(instructions):
                    inst_index = 0
        

        def prime_factors(number,itr, nums = None):
            if nums is None:
                nums = []
            if itr == 1:
                nums.append(number)
                return nums
            if number % itr == 0:  #if given number divided by itr or not
                new_number = int(number/itr)
                nums = prime_factors(itr, int(sqrt(itr)+1), nums)
                return prime_factors(new_number, int(sqrt(new_number)+1),nums)
            return prime_factors(number, itr-1, nums)
        
        factors = [prime_factors(x, int(sqrt(x)+1)) for x in loop_lengths]
        unique_factors = set()
        for f in factors:
            unique_factors.update(f)

        total = prod(unique_factors)

    print(f'{mode} : {total}')

if __name__ == "__main__":
    main('gold')