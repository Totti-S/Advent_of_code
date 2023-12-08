from utilities.get_data import get_data
import re
from math import sqrt, prod
def main(mode='silver', data_type=''):
    data = get_data(__file__, data_type)

    instructions = data.pop(0)
    data.pop(0)

    nodes = {}
    for line in data:
        node, L, R = re.findall(r'\w+', line)
        nodes[node] = (L,R)
    
    index, total = 0, 0
    current_position = 'AAA'
    while True:
        move = instructions[index]
        current_position = nodes[current_position][(move == 'R')]   # NOTE Boolean operation:
        total += 1                                            # False -> Left, True -> Right
        index += 1
        if current_position == 'ZZZ':
            break
        if index == len(instructions):
            index = 0

    print(f'Silver : {total}')

    starting_positions = [node for node in nodes if node.endswith('A')]
    loop_lengths = []
    # Knowing something about the solution we can assume that first we hit endpoint 
    for current_position in starting_positions:
        index, total = 0, 0
        end_point_found = False
        while True:
            move = instructions[index]
            current_position = nodes[current_position][(move == 'R')]   # NOTE Boolean operation:
            if current_position.endswith('Z'):                          # False -> Left, True -> Right
                if end_point_found:
                    loop_lengths[-1] = (total - loop_lengths[-1])
                    break
                end_point_found = True
                loop_lengths.append(total)

            total += 1
            index += 1
            if index == len(instructions):
                index = 0
        
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